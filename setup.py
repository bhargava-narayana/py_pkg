import os
from setuptools import setup, find_packages

def get_root_dir() -> str:
    return os.path.abspath(os.path.dirname(__file__))

def read(real_pth: str) -> str:
    here = get_root_dir()
    with open(os.path.join(here, real_pth), "r") as fp:
        return fp.read()

def get_py_ver() -> str:
    return read(".python-version")

def get_dependencies() -> list:
    dep = list()
    cont = (read("requirements.txt")).split(os.linesep)
    for _ in cont:
        if (not _.startswith("#")) and (len(_) !=0):
            dep.insert(len(dep), _)
    return dep

def get_pkg_ver() -> str:
    return read("py_pkg/__version__")

setup(name="testpkg",
      version=get_pkg_ver(),
      description="python test pkg",
      long_description=read("README.rst"),
      license="MIT",
      url="https://github.com/bhargava-narayana/py_pkg",
      author="Bhargava Narayana",
      pkg_dir={"": "pkg"},
      packages=find_packages(
                             where="py_pkg",
                             exclude=["docs",]
                            ),
      include_data_files=True,
      install_requires=get_dependencies(),
      entry_points={
          "console_scripts": [
              "test_pkg=py_pkg.main:main",
              ]
          },
      zip_safe=False,
      python_requires=f"=={get_py_ver()}",
    )
