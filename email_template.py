import sys
from premailer import Premailer

def email(html_file, css_file):
    html = open(html_file).read()
    mailer = Premailer(html, external_styles=css_file)
    return mailer.transform()

if __name__ == '__main__':
    print email(sys.argv[1], sys.argv[2])
