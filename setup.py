import os
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(HERE, 'requirements.txt'), "r") as fp:
    install_reqs = fp.read().splitlines()

setuptools.setup(
    name="liwc-text-analysis",
    version="1.0.2",
    author="Evan Lalopoulos",
    author_email="evan.lalopoulos.2017@my.bristol.ac.uk",
    description="A python package for the Linguistic Inquiry and Word Count (LIWC) dictionary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evanll/liwc-text-analysis-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_reqs
)
