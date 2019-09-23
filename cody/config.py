import os
import json
import random
import string

from pathlib import Path


CODY_FOLDER = os.path.join(str(Path.home()), '.cody')

os.makedirs(CODY_FOLDER, exist_ok=True)

CONFIG_FILE = os.path.join(CODY_FOLDER, '.cody')


def generate_token():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(32))


def read():
    if not os.path.isfile(CONFIG_FILE):
        return None
    with open(CONFIG_FILE) as config_file:
        return json.loads(config_file.read())


def write(project_name, project_path, slack_hook):
    token = generate_token()
    with open(CONFIG_FILE, 'w') as config_file:
        config_file.write(json.dumps({
            'project_name': project_name,
            'project_path' : project_path,
            'token' : token,
            'slack_hook': slack_hook
        }, sort_keys=True, indent=4))
    print ("Configuration is finished! 🎉")
    print ("Your project name is ", project_name)
    print ("Your project path is ", project_path)
    print ("Your token is ", token)
    print ("Your Slack hook is ", slack_hook)
