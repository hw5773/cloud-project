import socket
import threading
import argparse
import logging

SUCCESS = 1
FAILURE = -1
BUFFER_SIZE = 1024

# do_handshake: (message * server socket * client's address/port number) -> context
def do_handshake(msg, server, conn):
    sisn = random.randint(1, 1000000000)

    ...

    return ctxt

# handle_content_protocol: (message * server socket * client's address/port number) -> success(1) / failure (-1)
def handle_content_protocol(msg, server, conn):
    return ret

def run(addr, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((addr, port))

    logging.info("[*] Server is Listening on {}:{}".format(addr, port))

    # context_storage: identifier of a context -> context
    context_storage = {}

    while True:
        msg, conn = server.recvfrom(BUFFER_SIZE)
        logging.info("[*] Server accept the connection from {}:{}> {}".format(conn[0], conn[1], msg))

        saddr = ...
        sport = ...
        caddr = conn[0]
        cport = conn[1]

        identifier = "{}:{}-{}:{}".format(saddr, sport, caddr, cport)

        if identifier not in context_storage:
            ctxt = do_handshake(msg, server, conn)
            context_storage[identifier] = ctxt
        else:
            ctxt = context_storage[identifier]
            ret = handle_content_protocol(msg, server, conn)

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
