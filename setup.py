from esky import bdist_esky
from distutils.core import setup

setup(name="asmd",
      version="1.0.0",
      scripts=["asmd.py","mods/config.py"],
      options={"bdist_esky":{"includes":[]}},
     )
