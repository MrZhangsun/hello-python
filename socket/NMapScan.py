# coding=utf-8
import nmap
import optparse


def map_scan(tgt_host, tgt_port):
    scanner = nmap.PortScanner(nmap_search_path=('nmap', r"E:\developTools\python27\nmap\nmap.exe"))
    scanner.scan(tgt_host, tgt_port)
    state = scanner[tgt_host]['tcp'][tgt_port]['state']
    print '[*] %s tcp/%d' % (tgt_host, tgt_port)


# 格式化命令行参数
def param_parser():
    parser = optparse.OptionParser("-H <host> -p <port>")
    parser.add_option("-H", dest="tgt_host", type="string", help="specify target host")
    parser.add_option("-p", dest="tgt_port", type="string", help="specify target port[s] separated by comma")
    options, args = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_ports = options.tgt_port.split(",")
    return tgt_host, tgt_ports


def main():
    tgt_host, tgt_ports = param_parser()
    if tgt_host is None or tgt_ports[0] is None:
        print "[-] You must specify a target host and port."
        exit(0)
    for port in tgt_ports:
        map_scan(tgt_host, int(port))


if __name__ == '__main__':
    main()