import os
from setuptools import setup

version = "2.0.2"

current_directory = os.path.dirname(__file__)


try:
    with open(os.path.join(current_directory, 'rev.txt')) as file:
        for line in file: version = "{}-{}".format(version,line.strip());break
except:
    pass

setup(
    name="rust_webrcon",
    author='thegreatstorm',
    url='https://github.com/thegreatstorm/rust_rcon_lib',
    version="1.0.0.1",
    packages=["rust_webrcon"],
    python_requires='>=3.6',
    platforms=['Windows', 'Linux', 'OSX'],
    description='Tried of trying to find working rust web rcon for python look no further.',
    keywords='Rust web rcon interaction tool',
    include_package_data=True,
    install_requires=[
        "websocket-client >= 0.54.0"
    ]
)
