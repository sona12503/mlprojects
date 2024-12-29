from setuptools import setup, find_packages
from typing import List

hyphen_e = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements to me '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)

    return requirements


setup( 
    name ="mlprojectss",
    version = '0.0.1',
    author_name = "sonam",
    author_email = "bhardwajsonam2808@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)