'''setup.py is used to tell Python how to install and package a project.
In simple terms, it is the file that gives your project its name, version, 
and dependencies, so tools like pip know how to set it up correctly'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will retun list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from the files
            lines=file.readlines()
            # proceed each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('requirements.txt is not found')

    return requirement_lst

setup(
    name="Networksecurity",
    version="0.0.1",
    author="ramsai",
    author_email="ponugotiramsai@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

