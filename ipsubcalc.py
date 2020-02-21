# coding=utf-8
import ipaddress
import sys


def ipsubclac(ipadd):


    try:

        ip = ipaddress.IPv4Network(ipadd, strict=False)
        firstoct = int(str(ip).split('.')[0])
        ipclass = ''


        if firstoct == 127:
            return print("This is Loopback adress")

        elif firstoct >= 1 and firstoct <= 126:
            ipclass = "Class: A"

        elif firstoct >= 128 and firstoct <= 191:
            ipclass = "Class: B"

        elif firstoct >= 192 and firstoct <= 223:
            ipclass = "Class: C"

        elif firstoct >= 224 and firstoct <= 239:
            ipclass = "Class D: Reserved for Multicasting"

        else:
            ipclass = "Class E: Experimental-used for research"

    except ipaddress.AddressValueError:
        return print("Invalid IP")

    except ipaddress.NetmaskValueError:
        return print("Invalid Subnet Mask")

    print("Network IP address: {}".format(ip.network_address))
    print("Subnet mask: {}".format(ip.netmask))
    print("Broadcast address: {}".format(ip.broadcast_address))
    print("Usable IP address range: {}".format(ip.network_address + 1) + "-{}".format(ip.broadcast_address -1))

    print("Total number of Hosts: {}".format(ip.num_addresses))
    print("Number of Usable Hosts: {}".format(ip.num_addresses - 2))
    print("IP {}".format(ipclass))


def main():
    ipsubclac(sys.argv[1])

if __name__ == ('__main__'):
    main()
