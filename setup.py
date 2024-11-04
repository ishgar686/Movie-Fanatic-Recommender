from setuptools import setup

with open("reader.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "ISHAAN GARG"
CODE_REPOSITORY = "repo"
REQUIREMENTS = ["streamlit"]

setup(
    name = CODE_REPOSITORY,
    version = "0.0.1",
    author = AUTHOR_NAME, 
    author_email = "igarg@ucsd.edu",
    description = "Movie recommender system website",
    long_description_content_type= "text/markdown",
    packages = [CODE_REPOSITORY],
    python_requires = ">= 3.7",
    install_requires = REQUIREMENTS,
)