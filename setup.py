from os import path
from setuptools import setup, find_packages


def get_long_description():
  here = path.abspath(path.dirname(__file__))
  with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="geo-bullseye",
    version="0.0.1",
    description="Find coordinates in a set of polygons.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/juangcr/geo-bullseye",
    author="Juan Cortés",
    author_email="juang.cortes@outlook.com",
    classifiers=[
        "Development Status :: 5 - Alpha",
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    keywords='geojson polygon coordinates geospatial',
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    extras_require={
        "test": [
            "coverage",
            "pytest",
            "black",
            "flake8",
            "mypy"
            ]
    },
)

