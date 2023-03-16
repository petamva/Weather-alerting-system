import requests
import re
import joblib
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import numpy as np
from utils.config import cfg
import utils.models as models
from utils.db import SessionFactory, Alerts


poly_temperature = joblib.load(cfg.path_trends.temperature)
poly_leafinfrared = joblib.load(cfg.path_trends.leafinfrared)


def get_history_array(values_dict, x):

    history_array = np.zeros(shape=(cfg.history, len(cfg.quantities)))
    
    for i, q in enumerate(cfg.quantities):
        history_array[:, i] = np.array(values_dict[q])
    if not np.isnan(history_array).any():
        history_array[:, 3] -= poly_temperature(x)
        history_array[:, 4] -= poly_leafinfrared(x)
        history_array = (history_array - np.array(cfg.mean)) / np.array(cfg.std)
        return history_array


def get_history(root, sensor_id, x):

    values_dict = {}
    for child in root:
        try:
            quant = cfg.sensors[sensor_id]['quantities'][child.attrib['id']]
        except KeyError:
            continue
        if quant in cfg.quantities:
            values_dict[quant] = []
            for grandchild in child:
                try:
                    values_dict[quant].append(float(grandchild.text))
                except TypeError:
                    return None
    if len(values_dict.keys()) != len(cfg.quantities):
        return None
    for key in values_dict.keys():
        if len(values_dict[key]) < 5:
            return None
        values_dict[key] = values_dict[key][-5:]
    return get_history_array(values_dict, x)


# def get_preds(farm, model = models.weather_model):

#     time_now = datetime.now().replace(microsecond=0, second=0, minute=0)
#     time_start = time_now - timedelta(hours=10)
#     time_start_string = datetime.strftime(time_start, '%Y%m%dT%H:%M:%S')
#     x = int((time_now - datetime(*cfg.start)).total_seconds()/3600) + cfg.target
        
#     login = requests.get(url=cfg.url, params=cfg.params_login)
#     session_id = re.search('(?<=<string>)(.+?)(?=</string>)', login.text).group()

#     params_get_data = {
#         'function' : 'getdata',
#         'session-id' : session_id,
#         'id' : cfg.farms[farm],
#         # 'id' : '753',
#         'date' : time_start_string,
#         'slots' : '10000'
#     }

#     data = requests.get(url=cfg.url, params=params_get_data)

#     params_logout = {
#         'function' : 'logout',
#         'session-id' : session_id,
#         'mode' : 't'
#     }

#     logout = requests.get(url=cfg.url, params=params_logout)

#     tree = ET.ElementTree(ET.fromstring(data.text))
#     root = tree.getroot()

#     batch = get_history(root, int(cfg.farms[farm]), x)
#     if isinstance(batch, np.ndarray): 
#         batch = batch.reshape((1,) + batch.shape)
#         predictions = model.predict(batch)[0]
#         true_predictions = (predictions * np.array(cfg.std)) + np.array(cfg.mean)
#         true_predictions[3] += poly_temperature(x)
#         true_predictions[4] += poly_leafinfrared(x)
#         pred_dict = dict(zip(cfg.quantities, true_predictions.round(decimals=2)))
#         with SessionFactory() as session:
#             session.add(Predictions(**pred_dict))
#             session.commit()
#     else:
#         pass


def alerts(farm, model = models.weather_model):
    
    farm_int = int(cfg.farms[farm])
    time_now = datetime.now().replace(microsecond=0, second=0, minute=0)
    time_start = time_now - timedelta(hours=10)
    time_start_string = datetime.strftime(time_start, '%Y%m%dT%H:%M:%S')
    x = int((time_now - datetime(*cfg.start)).total_seconds()/3600) + cfg.target
        
    login = requests.get(url=cfg.url, params=cfg.params_login)
    session_id = re.search('(?<=<string>)(.+?)(?=</string>)', login.text).group()

    params_get_data = {
        'function' : 'getdata',
        'session-id' : session_id,
        'id' : cfg.farms[farm],
        'date' : time_start_string,
        'slots' : '10000'
    }

    data = requests.get(url=cfg.url, params=params_get_data)

    params_logout = {
        'function' : 'logout',
        'session-id' : session_id,
        'mode' : 't'
    }

    logout = requests.get(url=cfg.url, params=params_logout)

    tree = ET.ElementTree(ET.fromstring(data.text))
    root = tree.getroot()
    table_fields = ['Timestamp', 'FarmKey', 'SensorKey', 'SensorValue']
    batch = get_history(root, int(cfg.farms[farm]), x)

    if isinstance(batch, np.ndarray):
        batch_ = batch.reshape((1,) + batch.shape)
        predictions = model.predict(batch_)[0]

        values_normalized = np.stack((predictions, batch[-1]), axis=0)
        values = (values_normalized * np.array(cfg.std)) + np.array(cfg.mean)
        values[:, 3] += poly_temperature(x)
        values[:, 4] += poly_leafinfrared(x)
        alerts_index = np.abs(values[0] - values[1]) > np.array(cfg.thresholds)

        if any(alerts_index):            
            alerts = zip(np.array(cfg.quantities)[alerts_index], values[0].round(decimals=2)[alerts_index])
            with SessionFactory() as session:
                for alert in alerts:
                    sensor_key = list(filter(lambda x: cfg.sensors[farm_int]['quantities'][x] == alert[0], cfg.sensors[farm_int]['quantities']))[0]
                    values = (datetime.now(), farm_int, sensor_key, alert[1])
                    value_dict = dict(zip(table_fields, values))
                    session.add(Alerts(**value_dict))
                session.commit()