#!/usr/bin/python
from mailer import Mailer
from mailer import Message

class Mail(object):
    def __init__(self, mailer=Mailer('localhost'), from_email, to_email, subject, html):

        message = Message(From=from_email,
                          To=to_email,
                          charset="utf-8")
        message.Subject = subject
        message.Html = html
        message.Body = """Digestive doesn't support non-html emails. Sorry!"""

        sender = mailer
        sender.send(message)