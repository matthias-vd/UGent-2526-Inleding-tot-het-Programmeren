def dl(n):
    l=[]
    i=1
    while i!=n:
        if n%i==0:
            l.append(i)
        i+=1
    return l
def som_delers(n):
    return sum(dl(n))
def getalsoort(n):
    if som_delers(n)>n:
        return 'overvloedig'
    if som_delers(n)<n:
        return 'gebrekkig'
    return 'perfect'