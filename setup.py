from setuptools import setup, find_packages

__version__ = "0.1.5"

setup (
    name="pltbox",
    version=__version__,
    description="A toolbox for plotting stuff",
    author="Max Resing",
    author_email="pypi.org@maxresing.de",
    url="https://github.com/resingm/pltbox",
    packages=find_packages(),
    install_requires=[
        "matplotlib >= 3.8",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

