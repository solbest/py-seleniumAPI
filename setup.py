from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('api/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup( 
    name = 'linkedin_api', 
    packages = ['linkedin_api'], # this must be the same as the name above 
    version = version, 
    description = 'Selenium ChromeOS data scraping', 
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = 'Green Dev', 
    author_email = 'solbest205@gmail.com', 
    url = 'https://github.com/solbest/linkedin_api', # use the URL to the github repo 
    download_url = 'https://github.com/solbest/linkedin_api/dist/' + version + '.tar.gz', 
    keywords = ['linkedin', 'scraping', 'scraper'],
    classifiers = [], 
    install_requires=[package.split("\n")[0] for package in open("requirements.txt", "r").readlines()]
)

