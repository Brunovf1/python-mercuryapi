# python3 setup.py build

from distutils.core import setup, Extension
setup(name="mercuryapi", version="0.2",
      ext_modules=[Extension("mercury",
                             sources=["mercury.c"],
                             libraries=["mercuryapi", "ltkc", "ltkctm"],
                             include_dirs=['build/mercuryapi/include'],
                             library_dirs=['build/mercuryapi/lib'])])
