from mako.template import Template
from email_template import email

def render_collection(collection):
    template = open('templates/index.html').read()
    html = Template(template).render(collection=collection)
    return email(html, "templates/styles.css")

if __name__ == '__main__':
    from data_puller import IssueCollection
    collection = IssueCollection()
    print render_collection(collection)
