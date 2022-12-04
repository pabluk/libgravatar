from setuptools import setup


with open("README.rst") as file:
    long_description = file.read()


setup(
    name="libgravatar",
    version="1.0.1",
    author="Pablo Seminario",
    author_email="pablo@seminar.io",
    url="https://github.com/pabluk/libgravatar",
    license="GNU General Public License v3 (GPLv3)",
    description="A library that provides a Python 3 interface for the Gravatar API.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords="gravatar",
    packages=["libgravatar"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Bug Reports": "https://github.com/pabluk/libgravatar/issues",
        "Source": "https://github.com/pabluk/libgravatar",
        "Documentation": "https://libgravatar.readthedocs.io",
    },
)
