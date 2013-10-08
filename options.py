import sys 

class ParseError(Exception):
    pass

class MissingArgumentError(Exception):
    pass

class Options(object):
    def __init__(self, args):
        if len(args) < 2:
            raise MissingArgumentError
        parts = args[0].split('/')
        if len(parts) != 2:
            raise ParseError
        self.repository = parts[1]
        self.username = parts[0]
        self.emails = args[1:]
        

def parse(argv = None):
    if argv == None:
        argv = sys.argv[1:]


    return Options(argv)
