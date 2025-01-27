from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of packages to install for the project.
    """
    requirements = []
    with open(file_path) as file_obj:  # Corrected to use the file_path argument
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='SSP',
    version='0.0.1',
    description='My Python package',
    author='Allaudin',
    author_email='allu456654ansari@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Pass the actual file path
)
