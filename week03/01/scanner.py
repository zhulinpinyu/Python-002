from multiprocessing import cpu_count, Queue
from multiprocessing.pool import Pool
import ipaddress
import os
from socket import *
import sys


def check_port(addr):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(3)
    try:
        ret = sock.connect_ex((addr['ip'], addr['port'],))
        if ret == 0:
            print(f"{ip}:{addr['port']}")
    except Exception as e:
        print(e)

def scan_port(ip):
    p2 = Pool(4)
    for port in range(1,1025):
        p2.apply_async(check_port, args=({'ip': ip, 'port': port},))

    p2.close()
    p2.join()

def check_ip_status(host):
    resp = os.system(f'ping -c 1 {host}')
    if resp == 0:
        return host

if __name__ == "__main__":
    args = sys.argv[1:]
    #设置默认值
    concurrence_count = cpu_count()

    for i in range(len(args)):
        if args[i] == '-n':
            concurrence_count = int(args[i+1])
        if args[i] == '-f':
            cmd = args[i+1]
        if args[i] == '-ip':
           [start_ip_str, end_ip_str] = args[i+1].split('-')
           start_ip = int(ipaddress.ip_address(start_ip_str))
           end_ip = int(ipaddress.ip_address(end_ip_str))
        if args[i] == '-w':
            output_path = args[i+1]

    if concurrence_count:
        p = Pool(concurrence_count)
    else:
        p = Pool(cpu_count())
    result = []
    for i in range(start_ip, end_ip+1):
        ip = ipaddress.ip_address(i)
        result.append(p.apply_async(check_ip_status, args=(ip,)))

    p.close()
    p.join()

    for ret in result:
        host = ret.get()
        if host:
            scan_port(str(host))
