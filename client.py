import socket
import argparse
import logging
import threading
import random
import json
from context import Context

SUCCESS = 1
FAILURE = -1
BUFFER_SIZE = 1024

def do_handshake(client, conn):
    cisn = random.randint(1, 1000000000)

    # SYN
    flag = 1
    ack = 0
    msg = b''
    msg += flag.to_bytes(1, byteorder="big")
    msg += cisn.to_bytes(4, byteorder="big")
    msg += ack.to_bytes(4, byteorder="big")

    logging.debug("flag: {}".format(flag))
    logging.debug("cisn: {}".format(cisn))
    logging.debug("ack: {}".format(ack))

    client.sendto(msg, conn)

    # SYN/ACK

    saddr = conn[0]
    sport = conn[1]
    caddr = client.getsockname()[0]
    cport = client.getsockname()[1]
    #ctxt = Context(saddr, sport, caddr, cport, sisn, cisn)

    #logging.info("identifier: {}".format(ctxt.get_identifier()))

    # Test context
    ctxt = Context("127.0.0.1", 7890, "127.0.0.1", 30000, 4001, 1002)
    
    return ctxt

# make_connection: (server's IP address * server's port numer) -> context
def make_connection(client, addr, port):
    conn = (addr, port)
    ctxt = do_handshake(client, conn)
    return ctxt

# do_user_creation: (server's IP address * server's port number * context) -> success (1)/failure (-1)
def do_user_creation(client, addr, port, ctxt):
    account = "account{}".format(random.randint(1, 100))
    password = "{}_password".format(account)

    body = {}
    body["password"] = password
    js = json.dumps(body)
    clen = len(js)

    msg = "POST /user/{}\r\nContent-Length:{}\r\n\r\n".format(account, clen)
    msg += js

    logging.debug("content request message: {}".format(msg))

    encap = ctxt.encap(msg)
    client.sendto(encap, (addr, port))

    ret = SUCCESS

    return ret


# do_signing_in: (server's IP address * server's port number * context) -> success (1)/failure (-1)
def do_signing_in(client, addr, port, ctxt):
    password = ""
    ret = FAILURE

    return ret

def client(addr, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ctxt = make_connection(client, addr, port)
    ret = do_user_creation(client, addr, port, ctxt)
    ret = do_signing_in(client, addr, port, ctxt)
    if ret == SUCCESS:
        content = request_content(client, addr, port, ctxt)
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
