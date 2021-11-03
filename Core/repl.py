from shlex import split as qsplit
import readline
import interp
init_prompt="HRZN-REPL >>> "
run_conflict = ""
def repl(prompt=init_prompt):
    while run_conflict != "stop":
        preask = input(prompt)
        ask = qsplit(preask, posix=False)
        interp.evalcode(ask)

    

    
