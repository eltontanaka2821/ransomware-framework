from setuptools import setup, find_packages

setup(
    name="rbprof",
    version="0.1.7",
    package_dir={"": "src"},  # Look for packages in the `src/` directory
    packages=find_packages(where="src"),  # Find packages in `src/`
    install_requires=[
        # Add dependencies here
    ],
    description="A cybersecurity framework for ransomware behavioral profiling.",
    author="Elton Mukarati",
    author_email="eltontanakamukarati@gmail.com",
    url="https://github.com/eltontanaka2821/ransomware-framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)