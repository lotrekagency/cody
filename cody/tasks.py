import os
from huey import SqliteHuey
from cody.config import CODY_FOLDER

huey = SqliteHuey(filename=os.path.join(CODY_FOLDER, '.cody.db'))

@huey.task()
def deploy_app(path):
    import time
    time.sleep(10)
    print (path)
