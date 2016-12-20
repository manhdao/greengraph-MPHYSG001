from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "1.0",
    author = "Manh Dao (Marvin)",
    author_email = "ducmanhdao92@gmail.com",
    description = ("A demonstration of how to generate a graph of the proportion of green pixels "
    										"in a series of satellite images between two points"),
    long_description=read('README.md'),
    license = "MIT",
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse','numpy','geopy','stringIO','matplotlib']
)

