#!/usr/bin/python
from mailer import Mailer
from mailer import Message

class Mail(object):
    def __init__(self, from_email, to_emails, subject, html, mailer=None):
        if mailer is None:
            mailer = Mailer(host='localhost', port=1025)

        for to_email in to_emails:
            message = Message(From=from_email,
                              To=to_email,
                              charset="utf-8")
            message.Subject = subject
            message.Html = html
            message.Body = """Digestive doesn't support non-html emails. Sorry!"""

            sender = mailer
            sender.send(message)