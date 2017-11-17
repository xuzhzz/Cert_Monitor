import ssl
import socket
from .models import MonitorInfo
import datetime

def get_current_date():
    gmt_format = '%b  %d %H:%M:%S %Y GMT'
    return datetime.datetime.now().strftime(gmt_format)


def get_valid_days(c, e):
    gmt_format = '%b  %d %H:%M:%S %Y GMT'
    dt = datetime.datetime.strptime(e, gmt_format) - datetime.datetime.strptime(c, gmt_format)
    return dt.days


def get_all_certs():
    monitors = MonitorInfo.objects.all()
    certs_list = []
    for m in monitors:
        # print('current_date:  ', m.current_date)

        data = {
            'system_name': m.cert.system_name,
            'addr': m.cert.addr,
            'sn': m.cert.sn,
            'start_date': m.cert.start_date,
            'end_date': m.cert.end_date,
            'valid_days': get_valid_days(get_current_date(), m.cert.end_date),
        }
        certs_list.append(data)
    return certs_list


def parse_cert_info(server_name, port=443):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.check_hostname = True
    ctx.load_default_certs()

    s = socket.socket()
    # s = ctx.wrap_socket(s, server_hostname=server_name)
    try:
        s = ctx.wrap_socket(s, server_hostname=server_name)
        s.connect((server_name, int(port)))
        s.do_handshake()
        cert = s.getpeercert()
    except Exception:
        return None
    # s.do_handshake()
    # cert = s.getpeercert()
    return cert
