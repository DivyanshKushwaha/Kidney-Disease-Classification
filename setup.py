import setuptools


with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_USER_NAME = "DivyanshKushwaha"
SRC_REPO = "CnnClassfier"   # This will enable the local package as CnnClassifier, no need to add src folder while importing files.
AUTHOR_EMAIL = "jatinkushwaha309@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DivyanshKushwaha/Kidney-Disease-Classification",
    project_urls = {
        "Bug Tracker": "https://github.com/DivyanshKushwaha/Kidney-Disease-Classification/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)