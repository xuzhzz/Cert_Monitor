from __future__ import absolute_import
import requests
from .cert_utils import *

import logging
from celery import task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
# from celery.app import Celery
import datetime


URL = "http://oops.op.internal.gridsumdissector.com/apiv1/alert/"
TOKEN = 'QEvguvj6'
SOURCE = 'Certificate.Monitor'
TITLE = ['证书即将过期', '证书临近过期', '证书不兼容']
CONTENT = ['证书即将过期', '证书临近过期', '证书不兼容']


def alert(rank, emails=None, phones=None):
    alert = {
        "source": SOURCE,
        "token": TOKEN,
        "title": TITLE[rank-3],
        "content": CONTENT[rank-3],
        "severity": rank,
        "emails": emails,
        "phones": phones,
    }
    try:
        r = requests.post(URL, json=alert, timeout=2)
        if r.status_code == 200:
            print('Alert sent')
        else:
            print('Alert error', r.json())
    except TimeoutError:
        print('timeout!')


@task
def monitoring():
    # print('monitoringaaaa')
    monitors = MonitorInfo.objects.all()
    for monitor in monitors:
        # print(monitor.cert.addr)
        emails = monitor.email
        phones = monitor.phone
        if not monitor.cert.isCompatible:
            alert(5, emails, phones)

        end_date = monitor.cert.end_date
        valid_days = get_valid_days(get_current_date(), end_date)
        if valid_days <= 60 and valid_days > 30:
            alert(3, emails, phones)
        elif valid_days <= 30:
            alert(4, emails, phones)
