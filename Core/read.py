import interp
import shlex

def openfile(file):
    for line in open(file).readlines():
        fileevalcode = shlex.split(line, posix=False)
        interp.evalcode(fileevalcode)


