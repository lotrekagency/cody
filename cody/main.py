import argparse
import signal
import daemon
import lockfile
import os

from bottle import run
from cody.config import CODY_FOLDER, read as read_config, write as write_config
from cody.api import *
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def __locked_pidfile(filename):
    lock = lockfile.FileLock(filename)
    lock.acquire(-1)

    realfile = open(filename, "w")
    realfile.write(str(os.getpid()))
    realfile.close()

    yield

    os.remove(filename)
    lock.release()


def main():
    current_config = read_config()
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "stop", "showconfig"])
    args = parser.parse_args()
    pidfile = os.path.join(CODY_FOLDER, ".cody.pid")
    huey_pid_file = os.path.join(CODY_FOLDER, ".codyhuey.pid")
    huey_log_file = os.path.join(CODY_FOLDER, ".codyhuey.log")

    if args.action == "start":
        if not current_config:
            print ("🦊 Welcome to Cody!")
            project_name = input("🚧 Insert the project name: ")
            project_path = input("🏡 Insert the project path: ")
            slack_hook = input ("💬 Insert your Slack hook: ")
            write_config(project_name, project_path, slack_hook)
        bottle_context = daemon.DaemonContext(
            pidfile=__locked_pidfile(pidfile)
        )
        print ("🕰  Preparing cron tasks...")
        os.system(
            "huey_consumer.py cody.huey --logfile={0}&> /dev/null & echo $! > {1}".format(
                huey_log_file, huey_pid_file
            )
        )
        print ("🚀 Launching Cody...")
        with bottle_context:
            run(server='gunicorn', host='0.0.0.0', port=11001)

    if args.action == "stop":
        with open(pidfile, "r") as p:
            pid = int(p.read())
            os.kill(pid, signal.SIGTERM)
        with open(huey_pid_file, "r") as p:
            pid = int(p.read())
            os.kill(pid, signal.SIGTERM)
        print ("🎈 Bye bye Cody!")

    if args.action == "showconfig":
        print ("🦊 Cody configuration")
        if not current_config:
            print ("📭 Configuration is empty!")
        else:
            print ("Project name:", current_config['project_name'])
            print ("Project path:", current_config['project_path'])
            print ("Token:", current_config['token'])
            print ("Slack hook:", current_config['slack_hook'])
