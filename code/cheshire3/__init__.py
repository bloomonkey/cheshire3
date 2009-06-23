

# --- require print() and make all strings unicodes
#from __future__ import print_function
#from __future__ import unicode_literals

import sys, os

# Tests for Python 3.0 incompatibility
#sys.py3kwarning = True

# Ignore md5 DeprecationWarning from PyZ3950.yacc
from warnings import filterwarnings
filterwarnings('ignore', 'the md5 module is deprecated; use hashlib instead',  DeprecationWarning, 'yacc')

home = os.environ.get("C3HOME")

__name__ = "cheshire3"
__package__ = "cheshire3"

__all__ = ['database', 'documentFactory', 'document', 'exceptions',
           'documentStore', 'extractor', 'index', 'indexStore', 'logger',
           'normalizer', 'objectStore', 'parser', 'preParser',
           'protocolMap', 'record', 'recordStore', 'resultSet', 'resultSetStore',
           'server', 'sqlite', 'tokenizer', 'tokenMerger', 'transformer', 'user',
           'workflow', 'xpathProcessor']


import cheshire3.internal
# sps = cheshire3.internal.get_subpackages()

sps= ['web']

for sp in sps:
    # call import for on init hooks
    try:
        __import__("cheshire3.%s" % sp)
    except:
        pass
           

