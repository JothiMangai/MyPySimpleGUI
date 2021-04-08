def fw(fn,tasks):
    with open (fn,"w")as fp:
        for x in tasks:
<<<<<<< HEAD
            fp.write("%s \n"% x)
=======
            fp.write("%s \n "% x)
>>>>>>> 599b6fb00a94da06ceb0a9cac76a8dacd6685c15

def fr(fn):
    tasks=[]
    with open(fn,"r")as fp:
        lines=fp.readlines()
        for line in lines:
<<<<<<< HEAD
            tasks.append(line.strip("\n"))
=======
            tasks.append(line.strip("\n"))
>>>>>>> 599b6fb00a94da06ceb0a9cac76a8dacd6685c15
