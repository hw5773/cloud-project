class Context:
    def __init__(saddr, sport, caddr, cport, cisn):
        self.saddr = saddr
        self.sport = sport
        self.caddr = caddr
        self.cport = cport
        self.sisn = 0
        self.cisn = cisn
        self.id = "{}:{}-{}:{}".format(saddr, sport, caddr, cport)

    def get_identifier(self):
        return self.id
