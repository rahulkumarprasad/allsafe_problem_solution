from .models import AllsafeWebsite
import urllib3
from datetime import datetime

def get_status_code():
    try:
        today_date=datetime.now().date()
        http = urllib3.PoolManager()
        url="https://allsafe.in/"
        res = http.request('GET', url)
        status=res.status
        if status == 200 or status == 500:
            AllsafeWebsite(status=status,total_request=1).save()
    except Exception as e:
            return None
