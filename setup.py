import setuptools
import os.path
import re


with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join("EXOSIMS", "__init__.py"), "r") as f:
    version_file = f.read()

version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)

if version_match:
    version_string = version_match.group(1)
else:
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="EXOSIMS",
    version=version_string,
    author="Dmitry Savransky",
    author_email="ds264@cornell.edu",
    description="Exoplanet Imaging Mission Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsavransky/EXOSIMS",
    packages=setuptools.find_packages(exclude=["tests*", "tools*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
