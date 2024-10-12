from setuptools import find_packages,setup
from typing import List



def get_requirements()->List[str]:
    reuirements_list:List[str]=[]
    return reuirements_list

setup  (
    name='smart brake monitoring system',
    version="0.0.1",
    author="Sai Srivatsav",
    author_email="245122748001@mvsrec.edu.in",
    packages=find_packages(),
    install_requires=get_requirements #pymongo
)