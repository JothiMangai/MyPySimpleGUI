def fw(fn,tasks):
    with open (fn,"w")as fp:
        for x in tasks:
            fp.write(x)

def fr(fn):
    tasks=[]
    with open(fn,"r")as fp:
        lines=fp.readlines()
        for line in lines:
            tasks.append(line)