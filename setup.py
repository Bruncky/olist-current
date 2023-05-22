from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'numpy==1.19.2',
    'pandas==1.1.3']

setup(
    name='olist',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Olist reviews analysis'
)
