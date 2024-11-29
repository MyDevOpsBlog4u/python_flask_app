from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.3.0',
        'click==8.1.6',
        'itsdangerous==2.1.2',
        'Werkzeug==2.3.6',
        'Jinja2==3.1.2',
    ],
)

