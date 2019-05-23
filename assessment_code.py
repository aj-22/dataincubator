def getNumberOfSeq(n,k,j):
    return 1*(k-1)**(n-4)*1*(k-1)*1+1*(k-1)**(n-4)*(k-2)*(k-2)*1

def getNumberOfSeqFast(n,k,j):
    term=1
    modNum=10**10+7
    for i in range(n-4):
        term*=(k-1)
        term=term%modNum
    term*=((k-1)+(k-2)*(k-2))
    return term
