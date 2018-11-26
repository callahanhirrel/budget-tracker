from setuptools import setup, find_packages

readme = open("README.md", "r")
long_description = readme.read()
readme.close()

setup(
    name="BIRT - Budgets in Real Time",
    version="0.0",
    author="Callahan Hirrel",
    author_email="callahan.hirrel@gmail.com",
    description="Real time budget tracker for college academic departments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/callahanhirrel/budget-tracker",
    packages=find_packages(),
)
