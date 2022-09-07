from tkinter import *

def p_test(n):#returns 1if isprime
    try:
        if n>1:
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return 0
                    break
         
            return 1
        else:
            return 0
    except:
        return 0

    

class window:
        def __init__(self,master):
            self.num_value = StringVar()
            self.num_entry = Entry(master,bg='grey',textvariable=self.num_value)
            self.num_entry.config(width=10,font=("맑은고딕 25"))
            self.result_label =  Label(master,bg='white',fg='black',width='25',height='7',text=' ',font=("맑은고딕",30),wraplength=600)
            self.pr= Button(master, width=26,command=self.displayIsprime,bg='lightblue',height=2,text='소수 검사')
            self.go= Button(master, width=26,command=self.displayGolh,bg='darkblue',height=2,text='골드바흐 파티션',fg='white')
            self.ff = Button(master, width=26,command=self.displayFacn,bg='black',height=2,text='소인수분해',fg='white')
           # master.bind('<Return>',self.delstr)
        def delstr(self):
            self.num_value.set('')
        def pak(self):
            self.pr.place(x=430)
            self.go.place(x=430,y=41)
            self.ff.place(x=430,y=82)
            self.num_entry.place(x=200,y=0)
            self.result_label.place(x=0,y=150)
            self.num_value.set('')
        def getstring(self):
            try:
                return int(self.num_entry.get())
            except:
                return self.num_entry.get()
        def isprime(self,num):
            try:
                if num<=8000000000:
                    return ('{} is prime'.format(num) if p_test(num) else '{} is not prime'.format(num))
                else:
                    return '직접 계산해 보는것을 추천합니다.'
            except:
                return '뭐지버근가'
        def golh(self,num=0):        
            try:
                if num>5100000000:
                    return ('직접 계산해 보는것을 추천합니다.')
                if num<=2:
                    return ('입력값이 너무 작습니다.')
                elif num%2!=0:
                    return ('짝수를 입력하세요.')
                else:
                    b=(int)(num/2)
                    a=b
                    while a>1:
                        if p_test(b)==1 and p_test(a)==1:
                            return ('{}+{}'.format(a,b))
                            break
                        else:
                            a=a-1
                            b=b+1
            except Exception as e:
                return '뭐지 버근가'
        def facn(self,num=2):
            
            try:
                if num>5100000000:
                    return ('직접 계산해 보는것을 추천합니다.')
                if num<=2:
                    return (num)    
                else:
                    d=2
                    rstr = ''
                    x=num

                    while(d<=x):

                        if x % d == 0:
                            rstr=rstr+'{}'.format(d)
                            x = x / d
                            break
                        else:
                            d = d + 1

                    while(d<=x):
                        if x % d == 0:
                            rstr=rstr+'x{}'.format(d)
                            x = x / d
                        else:
                            d = d + 1
                    return rstr
            except Exception as e:
                return('뭐지 버근가')
        def displayIsprime(self):
            self.result_label.config(text=self.isprime(self.getstring()))
        def displayGolh(self):
            self.result_label.config(text=self.golh(self.getstring()))
        def displayFacn(self):
            self.result_label.config(text=self.facn(self.getstring()))



root3 = Tk()
aa = window(root3)


aa.pak()


root3.title('prime calculator')
root3.option_add("*Font","맑은고딕 30")
root3.geometry('600x400')
root3.configure(bg='lightgray')






try:
    while True:
        
        root3.update()
except Exception as e:
    print("loop break : {}".format(e))
