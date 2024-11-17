import socket
import threading
import argparse
import logging

BUFFER_SIZE = 1024

def run(addr, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((addr, port))

    logging.info("[*] Server is Listening on {}:{}".format(addr, port))

    while True:
        msg, addr = server.recvfrom(BUFFER_SIZE)
        logging.info("[*] Server accept the connection from {}:{}> {}".format(addr[0], addr[1], msg.decode()))

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", metavar="<server's IP address>", help="Server's IP address", type=str, default="0.0.0.0")
    parser.add_argument("-p", "--port", metavar="<server's open port>", help="Server's port", type=int, required=True)
    parser.add_argument("-l", "--log", metavar="<log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)>", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    log_level = args.log
    logging.basicConfig(level=log_level)

    run(args.addr, args.port)

if __name__ == "__main__":
    main()
