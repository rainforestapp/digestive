from mako.template import Template

def render_collection(collection):
    template = open('templates/index.html').read()
    return Template(template).render(collection=collection)
