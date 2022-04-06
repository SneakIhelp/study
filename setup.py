from distutils.core import setup
import py2exe
 
setup(
    windows=[{"script":"love.py"}],
    options={"py2exe": {"includes":["sip"]}}
)