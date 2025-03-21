# setup.py
from setuptools import setup, find_packages

setup(
    name="ransomware-framework",  # Replace with your package name
    version="0.1.0",              # Initial version
    author="Elton Tanaka Mukarati",
    author_email="eltontanakamukarati@gmail.com",
    description="A Python package for demonstrating a ransomware framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eltontanaka2821/ransomware-framework",  # Replace with your repo URL
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify Python version compatibility
    install_requires=[],      # List dependencies here (if any)
)