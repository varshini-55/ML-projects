from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirements=line.strip()
                ## Ignore empty lines -e.
                if requirements and requirements!= '-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vijaya Varshini",
    author_email="vijayavarshini55@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)