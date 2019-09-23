import os
import requests
import json
from huey import SqliteHuey
from cody.config import CODY_FOLDER

from cody.shell import execute_commands


huey = SqliteHuey(filename=os.path.join(CODY_FOLDER, '.cody.db'))

@huey.task()
def deploy_app(project_name, path, slack_hook):
    (output, exit_code) = execute_commands([os.path.join(path, 'cody.sh')])
    if exit_code == 0:
        text = "🦊 Project {0}\n✅ Deploy successful".format(project_name)
    else:
        text = "🦊 Project {0}\n❌ Deploy has failed!\n📄 Exit code {1} - {2}".format(
            project_name, exit_code, output
        )
    payload = {'text': text}
    print (slack_hook)
    r = requests.post(
        slack_hook,
        data=json.dumps(payload)
    )
    print (r)
