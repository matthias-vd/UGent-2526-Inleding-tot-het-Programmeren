def gemeenschappelijke_karakters(wa,wb):
    res=0
    sla=list(set(wa))
    slb=list(set(wb))
    for e in sla:
        if e in slb:
            res+=1
    return res