# coding=utf-8
import optparse
from socket import *


# 尝试连接
def conn_scan(target_host, target_port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((target_host, target_port))
        conn_socket.send("hello python\r\n")
        response = conn_socket.recv(1024)

        print "%s response message: %s" % (target_host, str(response))
        print "[+]%d/tcp open" % target_port
        conn_socket.close()
    except StandardError, e:
        print e
        print "[-]%d/tcp closed" % target_port


# 端口扫描
def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except StandardError:
        print "[-] Cannot resolve %s: Unknown host" % tgt_host
        return

    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print "\n[+] Scan Results for:%s" % tgt_name[0]
    except StandardError:
        print "\n[-] Scan Results for:%s" % tgt_ip
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print "Scanning port %d" % tgt_port
        conn_scan(tgt_host, tgt_port)


# 格式化命令行参数
def param_parser():
    parser = optparse.OptionParser("-H <host> -p <port>")
    parser.add_option("-H", dest="tgt_host", type="string", help="specify target host")
    parser.add_option("-p", dest="tgt_port", type="string", help="specify target port[s] separated by comma")
    options, args = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_ports = options.tgt_port.split(",")
    return tgt_host, tgt_ports


# 程序入口
def main():
    tgt_host, tgt_ports = param_parser()
    if tgt_host is None or tgt_ports[0] is None:
        print "[-] You must specify a target host and port."
        exit(0)
    for i in range(0, len(tgt_ports)):
        tgt_ports[i] = int(tgt_ports[i])

    port_scan(tgt_host, tgt_ports)


if __name__ == '__main__':
    main()
