from django.shortcuts import render
from .cert_utils import *
from .models import CertInfo, MonitorInfo
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'monitor/index.html')


def create_monitor(request):
    data = request.POST
    addr = data.get('domain', None)
    port = data.get('port', None)
    system_name = data.get('system_name', None)
    email = data.get('email', None)
    phone = data.get('phone', None)
    cert_info = parse_cert_info(addr, port)
    if not cert_info:
        return HttpResponse('请填写正确的证书')
    ci = CertInfo(sn=cert_info['serialNumber'], organization=cert_info['issuer'], addr=addr,
                  system_name=system_name, start_date=cert_info['notBefore'], end_date=cert_info['notAfter'])
    ci.save()

    gmt_format = '%b  %d %H:%M:%S %Y GMT'
    current_date = datetime.datetime.now().strftime(gmt_format)
    mi = MonitorInfo(cert=ci, email=email, phone=phone)
    mi.save()
    return render(request, 'monitor/detail.html',
                  context={'certs_list': get_all_certs(), 'current_date': get_current_date()})


def certs_detail(request):
    return render(request, 'monitor/detail.html',
                  context={'certs_list': get_all_certs(), 'current_date': get_current_date()})

