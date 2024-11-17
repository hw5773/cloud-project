import socket
import argparse
import logging
import threading

def make_connection(addr, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn = (addr, port)
    client.sendto("Hello world!".encode(), conn)

def run(addr, port, number):
    for _ in range(number):
        thread = threading.Thread(target=make_connection, args=(addr,port,))
        thread.start()

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", metavar="<server's address>", help="Server's address", type=str, required=True)
    parser.add_argument("-p", "--port", metavar="<server's port>", help="Server's port", type=int, required=True)
    parser.add_argument("-n", "--number", metavar="<# of simultaneous clients>", help="# of simultaneous clients", type=int, required=True)
    parser.add_argument("-l", "--log", metavar="<log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)>", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    log_level = args.log
    logging.basicConfig(level=log_level)

    run(args.addr, args.port, args.number)
    
if __name__ == "__main__":
    main()
