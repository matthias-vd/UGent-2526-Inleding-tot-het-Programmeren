def bereken_score(scores):
    l=[e for e in scores if 0<=e<=100]
    l.remove(max(l))
    l.remove(min(l))
    return int(round(sum(l)/len(l),0))