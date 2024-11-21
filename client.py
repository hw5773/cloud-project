import socket
import argparse
import logging
import threading
import random
import context

SUCCESS = 1
FAILURE = -1
BUFFER_SIZE = 1024

def do_handshake(client, conn):
    cisn = random.randint(1, 1000000000)
    saddr = conn[0]
    sport = conn[1]
    caddr = ...
    cport = ...
    ctxt = context.Context(saddr, sport, caddr, cport, cisn)

    flag = 1
    ack = 0
    msg = b''
    msg += flag.to_bytes(1, byteorder="big")
    msg += isn.to_bytes(4, byteorder="big")
    msg += ack.to_bytes(4, byteorder="big")
    client.sendto(msg, conn)

    return ctxt

# make_connection: (server's IP address * server's port numer) -> context
def make_connection(addr, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn = (addr, port)
    ctxt = do_handshake(client, conn)
    return ctxt

# do_signing_in: (server's IP address * server's port number * context) -> success (1)/failure (-1)
def do_signing_in(addr, port, ctxt):
https://docs.google.com/spreadsheets/d/1neDIk6Bq0y6vH0Vlrve-EHEIfe9fv01IhzmesJFq5bI/edit?usp=sharing    username = ""
    password = ""
    ret = FAILURE

    return ret

def client(addr, port):
    ctxt = make_connection(addr, port)
    ret = do_signing_in(addr, port, ctxt)
    if ret == SUCCESS:
        content = request_content(addr, port, ctxt)
        if content:
            logging.info("Content: {}".format(content))
        else:
            logging.error("Error in requesting the content")

def run(addr, port, number):
    for _ in range(number):
        thread = threading.Thread(target=client, args=(addr,port,))
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
