from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pycoinlib",
    packages=find_packages(),
    version=0.1,
    license="MIT License",
    description="Python client for the coinlib.ai API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rich Atkinson",
    author_email="rich@airteam.com.au",
    url="https://github.com/atkinson/pycoinlib",
    download_url="",
    keywords=["crypto", "trading", "coinlib"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
