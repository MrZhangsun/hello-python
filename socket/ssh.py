import socket


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return None


def check_value(banner):
    if "FreeFloat Ftp Server (Version 1.00)" in banner:
        print "[+] FreeFloat FTP Server is vulnerable."
    elif "3Com 3CDamon FTP Server (Version 2.00)" in banner:
        print "[+] 3Com 3CDamon FTP Server is vulnerable."
    elif "Ability Server 2.34" in banner:
        print "[+] Ability FTP Server is vulnerable."
    elif "Sami FTP Server Version 2.0.2" in banner:
        print "[+] Sami FTP Server is vulnerable."
    else:
        print "[-] FTP Server is not vulnerable"
    return


def get_ips(num, rng, oip):
    if rng is None and len(rng) < 2:
        return None
    if num > 3:
        return None
    fs = oip.split(".")
    ip_list = []
    if num == 0:
        for_each(num, rng, fs, ip_list)
    elif num == 1:
        for_each(num, rng, fs, ip_list)
    elif num == 2:
        for_each(num, rng, fs, ip_list)
    elif num == 3:
        for_each(num, rng, fs, ip_list)

    return ip_list


def for_each(num, rng, fs, ip_list):
    for i in range(rng[0], rng[1], 1):
        fs[num] = i
        new_ip = str(fs[0]) + "." + str(fs[1]) + "." + str(fs[2]) + "." + str(fs[3])
        ip_list.append(new_ip)


def main():
    port = 22
    origin_ip = "139.169.141.5"
    ip_rng = (0, 256)
    ip_list = get_ips(3, ip_rng, origin_ip)
    for i in ip_list:
        banner = ret_banner(i, port)
        print banner
        if banner:
            check_value(banner)


if __name__ == '__main__':
    main()