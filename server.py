from aiohttp import web
from parser import *
import aiohttp_jinja2
import jinja2

app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('templates'))

@aiohttp_jinja2.template('index.html')
def handler(request):
    return {'title':'Vacancies','content':data_from_server}

app.add_routes([web.get('/', handler)])

web.run_app(app)






