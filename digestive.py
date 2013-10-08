import requests
import options
from data_puller import DataPuller

def main():
    try:
        opts = options.parse()
    except(options.ParseError, options.MissingArgumentError):
        print "Usage: python program.py rainforestapp/GitSatisfaction me@example.org"
        exit(1)

    puller = DataPuller(opts.username, opts.repository)
    print puller.users

if __name__ == '__main__':
    main()
