import json
from bottle import post, request
from cody.config import read as read_config


@post('/api/deploy')
def deploy():
    try:
        data = request.json
        current_config = read_config()
        if data['token'] == current_config['token']:
            return "OK"
        else:
            return "WRONG TOKEN"
    except json.decoder.JSONDecodeError:
        pass
