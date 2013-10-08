from mako.template import Template
from email_template import email

def render_collection(collection):
    template = open('digestive/templates/index.html').read()
    html = Template(template).render(collection=collection)
    return email(html, "digestive/templates/styles.css")

if __name__ == '__main__':
    from models import DigestData
    collection = DigestData()
    print render_collection(collection)
