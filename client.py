import socket
from datetime import datetime
import argparse

def send_timestamp(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    client_socket.sendall(timestamp.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Send local timestamp to the server.')
    # parser.add_argument('server_ip', type=str, help='IP address of the server')
    # parser.add_argument('server_port', type=int, help='Port of the server')
    # args = parser.parse_args()

    send_timestamp("50.17.60.150", 28557)
    # send_timestamp(args.server_ip, args.server_port)
