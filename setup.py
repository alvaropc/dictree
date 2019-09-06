from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'src/version.py')) as f:
    __version__ = f.read().strip().split("__version__=")[-1].replace('\"',"")


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = [line.strip() for line in f.read().splitlines()]

dictree_packages = [f"dictree.{package}" for package in find_packages(where=os.path.join(os.path.dirname(__file__), 'src'))]
dictree_packages.append("dictree")

setup(
    name='dictree',
    version=__version__,
    packages=dictree_packages,
    include_package_data=True,
    package_dir={"dictree": "src/"},
    install_requires=requirements,
    author='Álvaro Ponce',
    author_email="alvaropc63@gmail.com",
    description='Dictree is like dict but in graph format!'
)