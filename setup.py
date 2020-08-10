import os
from distutils import setup

version = "1.0.0.0"

current_directory = os.path.dirname(__file__)


try:
    with open(os.path.join(current_directory, 'rev.txt')) as file:
        for line in file: version = "{}-{}".format(version,line.strip());break
except:
    pass

setup(
    name="rust_rcon_lib",
    version=version,
    packages=["rust_rcon_lib", "rust_rcon_lib.utils"],
    include_package_data=True,
    install_requires=[
        "websocket-client >= 0.54.0"
    ]
)