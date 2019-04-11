# NOTE the `build` and `install` commands will not yet work with this setup script.

from setuptools import setup, find_packages

readme = open("../README.md", "r")
long_description = readme.read()
readme.close()

req_file = open("requirements.txt", "r")
requirements = req_file.read().split("\n")[:-1]
req_file.close()

setup(
    name="BudgetApp",
    version="0.0",
    author="Callahan Hirrel",
    author_email="callahan.hirrel@gmail.com",
    description="Real time budget tracker for college academic departments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/callahanhirrel/budget-tracker",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    license="GNU GPL",
)
