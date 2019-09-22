Cody
====

Cody is a lightweight microservice that you can install on your machines
to automate deploy requests with a simple POST request!

Installation
------------

::

    pip install cody

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

    curl -d '{"token":"MY_PROJECT_TOKEN"}' -H "Content-Type: application/json" -X POST http://localhost:11001/api/deploy

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

    Your project path is  .
    Your token is  decfFMB1QQtVDT7WxLhF5B4ySJ5SXkQo
