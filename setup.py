from distutils.core import setup, Extension

readme_conts = open("README.md", "U").read()
procname_ext = Extension("procname", ["procnamemodule.c"])

setup(name="procname", version="0.2",
      url="http://github.com/chemiron/python-procname/",
      author="Eugene A. Lisitsky",
      description="Set process titles in Python programs",
      long_description=readme_conts,
      ext_modules=[procname_ext])
