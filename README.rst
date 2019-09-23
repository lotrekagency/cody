Cody
====

Cody is our lightweight microservice that you can install on your
machines to automate deploy with a simple POST request using Gitlab 🦊!
You'll receive the results on Slack

Installation
------------

::

    pip install codycd

Before starting
---------------

Ensure you have port ``11001`` open

::

    ufw allow 11001

Ensure you have ``cody.sh`` script file inside your project where you
define your CD instructions! Then run ``Cody`` using

Start Cody
----------

::

    cody start

After configuration, try to execute a deploy

::

    curl -H "X-Gitlab-Token: MY_PROJECT_TOKEN" -X POST http://localhost:11001/api/deploy

Stop Cody
---------

::

    cody stop

Show configuration
------------------

::

    cody showconfig

It returns the current configuration

::

    Project name: Projectname
    Project path: /var/www/lotrek/myproject
    Token: f4k3t0k3n3v3rywH3r3
    Slack hook: https://hooks.slack.com/F4k3/W3BH00k
