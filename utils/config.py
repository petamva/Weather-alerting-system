from types import SimpleNamespace

cfg = SimpleNamespace(
    url = 'http://agro4sensors.athenarc.gr:8080/addUPI',
    db_url = "mysql+pymysql://petamva:Pet%40mv%40134679-852@kubem.ceti.gr:30002/spa_a4p_platform",
    farms = {
        'AthenaRC' : '753',
        'Chatzisavva' : '824',
        'Vourvoukeli' : '783'
        },
    sensors = {
        753 : { 
            'location' : 'AthenaRC', 
            'quantities' : {    
                '768' : 'DiffuseSolarRadAvg',
                '775' : 'SolarRadAvg',
                '769' : 'ParAvg',
                '770' : 'WindSpeedAvg',
                '771' : 'WindSpeedMax',
                '823' : 'GenericOutput',
                '772' : 'PrecipitationSum',
                '773' : 'SunshineSum',
                '774' : 'WindDirectionAvg',
                '777' : 'TemperatureAvg',
                '779' : 'TemperatureMax',
                '778' : 'TemperatureMin',
                '1032' : 'LeafInfraredAvg',
                '1034' : 'LeafInfraredMax',
                '1033' : 'LeafInfraredMin',
                # '780' : 'LeafInfraredAvg',
                '781' : 'RelHumidityAvg',
                '766' : 'SoilHumidity',
                '782' : 'LeafWetness',
            }
        },

        824 : {
            'location' : 'Chatzisavva',
            'quantities' : {    
                '844' : 'DiffuseSolarRadAvg',
                '851' : 'SolarRadAvg',
                '845' : 'ParAvg',
                '846' : 'WindSpeedAvg',
                '847' : 'WindSpeedMax',
                '848' : 'PrecipitationSum',
                '849' : 'SunshineSum',
                '850' : 'WindDirectionAvg',
                '852' : 'TemperatureAvg',
                '854' : 'TemperatureMax',
                '853' : 'TemperatureMin',
                '855' : 'LeafInfraredAvg',
                '1044' : 'LeafInfraredMax',
                '1043' : 'LeafInfraredMin',
                '856' : 'RelHumidityAvg',
                '842' : 'SoilHumidity_00',      
                '836' : 'SoilHumidity_01',      
                '838' : 'SoilHumidity_02',      
                '840' : 'SoilHumidity_03',      
                '857' : 'LeafWetness',
            }
        },

        783 : {
            'location' : 'Vourvoukeli',
            'quantities' : {
                '797' : 'DiffuseSolarRadAvg',
                '805' : 'SolarRadAvg',
                '798' : 'ParAvg',
                '799' : 'WindSpeedAvg',
                '800' : 'WindSpeedMax',
                '801' : 'PrecipitationSum',
                '803' : 'SunshineSum',
                '804' : 'WindDirectionAvg',
                '1038' : 'TemperatureAvg',
                '1040' : 'TemperatureMax',
                '1039' : 'TemperatureMin',
                '809' : 'LeafInfraredAvg',
                '1042' : 'LeafInfraredMax',
                '1041' : 'LeafInfraredMin',
                '810' : 'RelHumidityAvg',
                '795' : 'SoilHumidity',
                # '817' : 'SoilHumidity - 515496',
                # '815' : 'SoilHumidity - 515499',
                # '813' : 'SoilHumidity - 515501',
                '811' : 'LeafWetness',
            }
        }
    },
    params_login = {
        'function' : 'login',
        'user' : 'a4p-spa-api-user',
        'passwd' : '@4p-sp@-@pi-p@ass',
        'version' : 1.2
    },
    start = (2022, 1, 20, 1, 0),
    path_model = './models/weather_no_trend_3h',
    history = 5,
    target = 2,
    path_trends = SimpleNamespace(
        temperature = './trends/poly_temperature.pkl',
        leafinfrared = './trends/poly_leafinfrared.pkl',
        ),
    quantities = ['DiffuseSolarRadAvg', 'SolarRadAvg', 'WindSpeedAvg', 'TemperatureAvg', 'LeafInfraredAvg', 'RelHumidityAvg', 'LeafWetness'],
    # thresholds = [110.410, 375.682, 1.951, 5.208, 11.162, 17.640, 2.75],
    thresholds = [110.410, 375.682, 1.951, 0, 0, 17.640, 2.75],
    # thresholds = [55, 300, 1, 3, 6, 10, 2],
    mean = [64.0454368, 197.34128975, 2.48948874, 17.92733688, 18.31286139, 57.03410028, 1.12660447],
    std = [85.88843086, 269.62228911, 1.87705166, 9.62852278, 12.66300433, 17.75180469, 2.82920876],
)
