class Context:
    def __init__(self, saddr, sport, caddr, cport, sseq, cseq):
        self.saddr = saddr
        self.sport = sport
        self.caddr = caddr
        self.cport = cport
        self.sseq = sseq
        self.cseq = cseq
        self.id = "{}:{}-{}:{}".format(saddr, sport, caddr, cport)

    def get_identifier(self):
        return self.id

    def encap(self, msg):
        flag = 3
        seq = self.cseq
        ack = self.sseq

        pkt = b''
        pkt += flag.to_bytes(1, byteorder="big")
        pkt += seq.to_bytes(4, byteorder="big")
        pkt += ack.to_bytes(4, byteorder="big")
        pkt += msg.encode("ascii")

        return pkt

    def decap(self, msg):
        flag = msg[0]
        seq = int.from_bytes(msg[1:5], byteorder="big")
        ack = int.from_bytes(msg[5:9], byteorder="big")

        # TODO: update the context

        cmsg = msg[9:].decode("ascii")

        return cmsg
