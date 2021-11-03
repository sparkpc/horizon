import shlex
class eval:
    scriptvars = {}
    lastcmp = -1
    als = {}
    tasks = {}
    mode = "RUN"
    nexttask = ""
def evalcode(code):
    if eval.mode == "RUN":
        if code[0] in eval.als: 
            acode = []
            for entry in range(len(eval.als[code[0]])):
                if eval.als[code[0]][entry] == "$":
                    acode.append(code[1])
                else:
                    acode.append(eval.als[code[0]][entry])
            evalcode(acode)

        if code[0] == "write":
            if code[1] == "1":
                with open("/dev/stdout", "w") as towrite:
                    try:
                        if code[3] == "+n":
                            towrite.write(code[2] + "\n")
                    except IndexError:
                        towrite.write(code[2])


        elif code[0] == "assign":
            eval.scriptvars[code[1]] = code[2]
        elif code[0] == "writev":
            with open("/dev/stdout", "w") as towrite:
                    try:
                        if code[3] == "+n":
                            towrite.write(eval.scriptvars[code[2]] + "\n")
                    except IndexError:
                        towrite.write(eval.scriptvars[code[2]])
        elif code[0] == "al":
            alname = code[1]
            alcode = code[2:]
            eval.als[alname] = alcode 

            


        elif code[0] == "cmp":
            if eval.scriptvars[code[1]] == eval.scriptvars[code[2]]:
                eval.lastcmp = 1
            else:
                eval.lastcmp = 0
        elif code[0] == "tcmp":
            if eval.lastcmp == 1:
                evalcode(code[1:])
        elif code[0] == "fcmp":
            if eval.lastcmp == 0:
                evalcode(code[1:])

        elif code[0] == "use":
            for line in open(code[1] + ".hrh").readlines():
                evalcode(shlex.split(line, posix=False))
        elif code[0] == "open":
            if code[1] == "r":
                eval.scriptvars[code[2]] = open(code[3].strip("\"")).read()
                if code[4] == ">":
                    readcode = []
                    readcode[0] = code[5] 
                    print(readcode.append(code[2]))
            elif code[1] == "w":
                open(code[2].strip("\""), "w").write(code[3].strip("\""))
        elif code[0] == "read":
            if code[2] == "+prompt":
                open("/dev/stderr", "w").write(input(code[3].strip("\"")))
     
            elif code[1] == "0":
                open("/dev/stdin", "w").write(input())
            elif code[1] == "1":
                open("/dev/stdout", "w").write(input())
            elif code[1] == "2":
                open("/dev/stderr", "w").write(input())
        elif code[0] == "task":
            eval.nexttask = code[1]
            eval.tasks[eval.nexttask] = []
            eval.mode = "TASK"
        elif code[0] == "printasks":
            print(eval.tasks[eval.nexttask])
        elif code[0] == "dotask":
            for entry in eval.tasks[code[1]]:
                evalcode(entry)
    elif eval.mode == "TASK":
        if code[0] != "endtask":
            eval.tasks[eval.nexttask].append(code)
        elif code[0] == "endtask":
            eval.mode = "RUN"



