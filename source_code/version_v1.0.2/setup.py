from distutils.core import setup
import py2exe,sys,os

sys.argv.append('py2exe')
includes = ['redmine', 'wx']
setup(
    options = {'py2exe':
                {'bundle_files': 1,
                 'includes':includes
                 }},
    windows = ["main.py"],
    zipfile = None,
)
