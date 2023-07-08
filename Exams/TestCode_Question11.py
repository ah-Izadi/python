from operator import itemgetter
l = []

def myfunc(inp):
    while True: 
        l.append(tuple(inp.split(',')))
        if "*" in inp:
            break
    return(l,itemgetter(1,2,3))

assert myfunc("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 *") == "[('Tom', '19', '80'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85')] operator.itemgetter(1, 2, 3)"