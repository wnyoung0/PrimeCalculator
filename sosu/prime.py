"""
all fuctions don't limit size of number.
"""




def test(n):
    """test if it's prime

    """
    try:
        if n>1:
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
                    break
         
            return True
        else:
            return False
    except:
        return False

def partition_h(num=0):
    """calculates goldbach partition

    returns higher prime number in partition
    returns -1 when number is smaller then 3 or is oddnumber
    also returns -1 when it's not number

    n - GoldbachPartition(n) is lower prime number
    """
    try:
        if num<=2:
            return -1
        elif num%2!=0:
            return -1
        else:
            b=(int)(num/2)
            a=b
            while a>1:
                if p_test(b)==1 and p_test(a)==1:
                    return b
                    break
                else:
                    a=a-1
                    b=b+1
    except Exception as e:
        return -1

def partition_l(num=0):
    """calculates goldbach partition

    returns lower prime number in partition
    returns -1 when number is smaller then 3 or is oddnumber
    also returns -1 when it's not number
    """
    try:
        if num<=2:
            return -1
        elif num%2!=0:
            return -1
        else:
            b=(int)(num/2)
            a=b
            while a>1:
                if p_test(b)==1 and p_test(a)==1:
                    return a
                    break
                else:
                    a=a-1
                    b=b+1
    except Exception as e:
        return -1



def factor(num=2):
    """factorize
     
    returns list
    first index is number of prime factor
    """
    n=0
    l = []
    l.append(n)
    try:
        if num<=2:
            l[0]=1
            l.append(num)
            return l
        else:
            d=2
            x=num
            while(d<=x):
                if x % d == 0:
                    l.append(d)
                    n=n+1
                    x = int(x / d)
                else:
                    d = d + 1

            l[0]=n
            return l
    except:
        return l