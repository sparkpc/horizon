import interp
import shlex

def openfile(file):
    for line in open(file).readlines():
       interp.evalcode(shlex.split(line, posix=False))


