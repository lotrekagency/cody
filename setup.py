from setuptools import setup, find_packages


setup(
    name='cody',
    version='0.1.0',
    url='https://github.com/lotrekagency/cody',
    install_requires=[
        'bottle==0.12.17',
        'gunicorn==19.9.0'
    ],
    description="Cody is a lightweight microservice that you can install on your machines to automate deploy requests with a simple POST request!",
    long_description=open('README.rst').read(),
    license="MIT",
    author="Lotrèk",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
