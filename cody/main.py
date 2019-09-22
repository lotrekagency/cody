from bottle import run
from cody.config import read as read_config, write as write_config
from cody.api import *


def main():
    print ("👽 Welcome to Cody!")
    current_config = read_config()
    if not current_config:
        project_path = input("🏡 Insert the project path: ")
        write_config(project_path)
    run(server='gunicorn', host='localhost', port=11001)
