def lees_scores():
    l=[]
    inp=input()
    while inp!='stop':
        l.append(int(inp))
        inp=input()
    return l
def bereken_score(scores):
    l=[]
    for e in scores:
        if e>=0 and e<=100:
            l.append(e)
    l.remove(max(l))
    l.remove(min(l))
    return int(round(sum(l)/len(l),0))