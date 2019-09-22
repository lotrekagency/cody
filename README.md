# Cody

Cody is a lightweight microservice that you can install on your machines to automate deploy requests with a simple POST request!

## Installation

    pip install cody

## Run

    cody start

## Give it a try

Ensure you have `cody.sh` script file inside your project where you define your CD instructions! Then run `Cody` using

    cody start

After configuration, try to execute a deploy

    curl -d '{"token":"MY_PROJECT_TOKEN"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/deploy
