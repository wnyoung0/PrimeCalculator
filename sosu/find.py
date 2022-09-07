


def prime(m=0):
    """find prime in range 1 to m+1

    first index is len of the list
    """
    l = [False,False] + [True]*(m)
    n=0
    ll = [n]
    try:

        if m<2:
            return ll
        for i in range(2,m+1):
            if l[i]:
                n+=1
                ll.append(i)
                for j in range(2*i,m+1,i):
                    l[j]=False
        ll[0]=n
        return ll
    except:
        return ll

def prime_byRange(s=0,e=0):
    """returns prime in range s to e+1

    first index is len of the list
    """
    n=0
    t=True
    l=[n]
    try:
        if s<2:
            s=2
        if(e<2 or e<s):
            return l
        for i in range(s,e+1):
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    t=False
                    break
            if t==True:
                n+=1
                l.append(i)
            t=True
        l[0]=n
        return l
    except:
        return l

def germain_prime(s=0,e=0):
    """returns germain prime in range s to e+1

    first index is len of the list
    """
    n=0
    t=True
    l=[n]
    try:
        if s<2:
            s=2
        if(e<2 or e<s):
            return l
        for i in range(s,e+1):
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    t=False
                    break
            if t==True:
                
                for j in range(2,int((2*i+1)**0.5)+1):
                    if (2*i+1)%j==0:
                        t=False
                        break
                if t==True:
                    n+=1
                    l.append(i)
            t=True
        l[0]=n
        return l
    except:
        return l

        

#def twin_prime(s=0,e=0):         #만들기 싫다. 진짜 싫다.
    #pass

def thprime(m=0):
    """returns mth prime

    returns 0 when input is wrong 
    """
    try:
        if m<1:
            return 0
        n=0
        i=2
        t=True
        while n<m:
            for j in range(2,int((i)**0.5+1)):
                if(i%j==0):
                    t=False
                    break
            i+=1
            if t:
                n+=1
            t=True
        return i-1
    except:
        return 0
