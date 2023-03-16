from apscheduler.schedulers.background import BlockingScheduler, BackgroundScheduler
from utils.utils import alerts
from utils.config import cfg
from datetime import datetime, timedelta

sched = BlockingScheduler(timezone="Europe/Athens")

if __name__ == '__main__':
    time_now = datetime.now()
    for i, farm in enumerate(cfg.farms.keys()):
        # sched.add_job(alerts, 'interval', args=[farm], start_date=time_now + timedelta(minutes=i), hours=1)
        sched.add_job(alerts, 'interval', args=[farm], start_date=time_now + timedelta(seconds= 15*i), minutes=5)
    sched.start()
