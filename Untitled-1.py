def f(s,l,r):
    if r-l == 1:
        return 1
    if right[l] == r-1:
        return 2*f(s,l+1,r-1)
    return f(s,l,right[l]+1) + f(s,right[l]+1,r)


f(s,0,n)