import json
from bottle import post, request

from cody.config import read as read_config
from cody.tasks import deploy_app


@post('/api/deploy')
def deploy():
    try:
        current_config = read_config()
        if request.headers.get('X-Gitlab-Token') == current_config['token']:
            deploy_app(
                current_config['project_name'],
                current_config['project_path'],
                current_config['slack_hook']
            )
            return "Deploy Started"
        else:
            return "Wrong Token"
    except json.decoder.JSONDecodeError:
        pass
