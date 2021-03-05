import sys
import os
import argparse
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP


def main():
    parser = argparse.ArgumentParser(description='PCAP reader')
    parser.add_argument('--pcap', metavar='<pcap file name>',
                        help='pcap file to parse', required=True)
    args = parser.parse_args()

    file_name = args.pcap
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)

    count = pcap_count_packets(file_name)
    print("packet count:", count)

    count, interesting = pcap_count_interesting(file_name)
    print("TCP/IP packets:", interesting)

    target_client = '192.168.1.137:57080'
    target_server = '152.19.134.43:80'

    count, interesting = pcap_count_conn(file_name, target_client, target_server)
    print("connection packets:", interesting)


    sys.exit(0)


def pcap_count_packets(file_name):
    count = 0
    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

    return count


def pcap_count_interesting(file_name):
    count = 0
    interesting_packet_count = 0

    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields:
            # LLC frames will have 'len' instead of 'type'.
            # We disregard those
            continue

        if ether_pkt.type != 0x0800:
            # disregard non-IPv4 packets
            continue

        ip_pkt = ether_pkt[IP]
        if ip_pkt.proto != 6:
            # Ignore non-TCP packet
            continue

        interesting_packet_count += 1

    return count, interesting_packet_count


def pcap_count_conn(file_name, client, server):
    (client_ip, client_port) = client.split(':')
    (server_ip, server_port) = server.split(':')

    count = 0
    interesting_packet_count = 0

    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1

        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields:
            # LLC frames will have 'len' instead of 'type'.
            # We disregard those
            continue

        if ether_pkt.type != 0x0800:
            # disregard non-IPv4 packets
            continue

        ip_pkt = ether_pkt[IP]

        if ip_pkt.proto != 6:
            # Ignore non-TCP packet
            continue

        if (ip_pkt.src != server_ip) and (ip_pkt.src != client_ip):
            # Uninteresting source IP address
            continue

        if (ip_pkt.dst != server_ip) and (ip_pkt.dst != client_ip):
            # Uninteresting destination IP address
            continue

        tcp_pkt = ip_pkt[TCP]

        if (tcp_pkt.sport != int(server_port)) and \
                (tcp_pkt.sport != int(client_port)):
            # Uninteresting source TCP port
            continue

        if (tcp_pkt.dport != int(server_port)) and \
                (tcp_pkt.dport != int(client_port)):
            # Uninteresting destination TCP port
            continue

        interesting_packet_count += 1

    return count, interesting_packet_count

if __name__ == '__main__':
    main()
