from setuptools import setup, find_packages

setup(
    name="nqueens-solver",
    version="0.1.0",
    author="Durkesh",
    author_email="durkeshpanuja@gmail.com",
    description="A Python library to solve the N-Queens problem",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/durkesh-datasci/n-queens-solver",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
