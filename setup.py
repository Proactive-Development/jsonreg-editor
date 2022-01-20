from distutils.core import setup # Need this to handle modules
import py2exe 
import os
import json
import jsonreg
import argparse
from tabulate import tabulate
from colorama import Fore, Back, Style
setup(
    options = {'py2exe': {'compressed': True}},
    console = [{'script': "src/main.py"}],
    zipfile = None,
)