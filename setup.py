from setuptools import setup, find_packages


setup(
    name='codycd',
    version='0.2.0',
    url='https://github.com/lotrekagency/cody',
    install_requires=[
        'bottle==0.12.17',
        'gunicorn==19.9.0',
        'python-daemon',
        'lockfile',
        'huey==2.1.2',
        'requests==2.22.0'
    ],
    description="Cody is a lightweight microservice that you can install on your machines to automate deploy requests with a simple POST request using Gitlab!",
    long_description=open('README.rst').read(),
    license="MIT",
    author="Lotrèk",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'cody = cody.main:main',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
