"""Flask server"""
from json import dumps
from flask import Flask, request

#from server.access_error import AccessError
from server.message import *
#from server.admin_userpermission_change import *
from server.auth import *
from server.channel import *
from server.search import *
from server.standup import *
from server.user import *


APP = Flask(__name__)

@APP.route('/echo/get', methods=['GET'])
def echo1():
    """ Description of function """
    return dumps({
        'echo' : request.args.get('echo'),
    })

@APP.route('/echo/post', methods=['POST'])
def echo2():
    """ Description of function """
    return dumps({
        'echo' : request.form.get('echo'),
    })

if __name__ == '__main__':
    APP.run()
