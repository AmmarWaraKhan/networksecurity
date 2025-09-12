"""
The setup.py file is an essential part of packaging
and distributing python projects. It is used by setuptools 
(or distutils in older python versions) 
to define the configuration of your project, 
such as its metadata, dependencies, and more
"""


from setuptools import setup, find_packages 
from typing import List

def get_requirements() -> List[str]:
   """This function will return the list of requirements
   mentioned in the requirements.txt file"""
   requirements_lst:List[str] = []
   try:
        with open("requirements.txt", "r") as file:
            #Read all lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
               requirements = line.strip()
               ## ignore empty lines and -e .
               if requirements and requirements != '-e .':
                   requirements_lst.append(requirements)
   except FileNotFoundError:
       print("The requirements.txt file is not found.")   

   return requirements_lst   


print (get_requirements())


setup(
    name = "Network Security Project",
    version = "0.0.1",
    author = "Ammar Wara Khan",
    author_email = "ammarwarakhan@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

