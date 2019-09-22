import argparse
import signal
import daemon
import lockfile
import os

from bottle import run
from cody.config import read as read_config, write as write_config
from cody.api import *
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def __locked_pidfile(filename):
    # Acquire the lockfile
    lock = lockfile.FileLock(filename)
    lock.acquire(-1)

    # Write out our pid
    realfile = open(filename, "w")
    realfile.write(str(os.getpid()))
    realfile.close()

    # Yield to the daemon
    yield

    # Cleanup after ourselves
    os.remove(filename)
    lock.release()


def main():
    current_config = read_config()
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "stop"])
    args = parser.parse_args()
    pidfile = os.path.join(
        str(Path.home()),
        ".cody.pid"
    )
    if args.action == "start":
        if not current_config:
            print ("👽 Welcome to Cody!")
            project_path = input("🏡 Insert the project path: ")
            write_config(project_path)
        print ("🚀 Launching Cody...")
        context = daemon.DaemonContext(
            pidfile=__locked_pidfile(pidfile)
        )
        with context:
            run(server='gunicorn', host='0.0.0.0', port=11001)
    if args.action == "stop":
        with open(pidfile, "r") as p:
            pid = int(p.read())
            os.kill(pid, signal.SIGTERM)
        print ("🛑 Bye bye Cody!")
