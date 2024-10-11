from setuptools import find_packages,setup



def get_requirements()->list[str]:
    reuirements_list=list[str]=[]
    return reuirements_list

setup  (
    name='smart brake monitoring system',
    version="0.0.1",
    author="Sai Srivatsav",
    author_email="245122748001@mvsrec.edu.in",
    packages=find_packages(),
    install_requires=get_requirements #pymongo
)