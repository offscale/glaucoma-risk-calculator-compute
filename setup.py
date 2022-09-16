from ast import parse
from distutils.sysconfig import get_python_lib
from functools import partial
from itertools import ifilter, imap
from os import path

from setuptools import find_packages, setup

if __name__ == "__main__":
    package_name = "glaucoma_risk_calc_compute"

    with open(path.join(package_name, "__init__.py")) as f:
        __author__, __version__ = imap(
            lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
            ifilter(
                lambda line: line.startswith("__version__")
                or line.startswith("__author__"),
                f,
            ),
        )

    to_funcs = lambda *paths: (
        partial(path.join, path.dirname(__file__), package_name, *paths),
        partial(path.join, get_python_lib(prefix=""), package_name, *paths),
    )

    setup(
        name=package_name,
        author=__author__,
        version=__version__,
        test_suite=package_name + ".tests",
        # dependency_links=['https://github.com/scikit-learn-contrib/py-earth/tarball/master#egg=pyearth-0.1.0'],
        install_requires=["numpy", "matplotlib", "scikit.learn"],  #'pyearth==0.1.0'
        packages=find_packages(),
        package_dir={package_name: package_name},
    )
