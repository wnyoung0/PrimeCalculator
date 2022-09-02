from tkinter import *


def p_test(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
                break
         
        return 1
    else:
        return 0
class window:
        def __init__(self,master):
            
            self.image1=''

            self.num_value = StringVar()
            self.num_value.set('')

            self.num_entry = Entry(master,bg='grey',textvariable=self.num_value)
            self.num_entry.config(width=10,font=("맑은고딕 25"))
            self.num_entry.pack()
            
            self.result_label =  Label(master,bg='white',fg='black')
            self.result_label.config(width='30',height='2',text='',font=("맑은고딕",30))
            self.result_label.pack(side='left')
            master.bind('<Return>',self.inp)

        def inp(self,event=None,*kwarrgs):
            
            try:
                self.ll = int(self.num_entry.get())
                self.lll= golh(self.ll)
                self.result_label.config(width=40,text="{}+{}".format(self.lll[0],self.lll[1]))
                self.num_value.set('')
            except ValueError:
                print("{}is not integer.".format(self.num_entry.get()))
                if self.num_entry.get()=='':
                    self.result_label.config(text='값을 입력해요')
                elif self.num_entry.get()=='O':
                    self.result_label.config(text='0과 O는 달라요')
                    self.num_value.set('')
                else:
                    self.result_label.config(text='{}은/는 정수가 아니에요'.format(self.num_entry.get()))
                    self.num_value.set('')
            except Exception as yee:
                print(yee)
                self.num_value.set('')
def golh(num=0):
    if num>2100000000:
        return ('%','Too Big')
    try:
        if num<=2:
            return ('%','Too Small')
        elif num%2!=0:
            return ('%','That`s Odd')
        else:
            b=(int)(num/2)
            a=b
            while a>1:
                if p_test(b)==1 and p_test(a)==1:
                    return (a,b)
                    break
                else:
                    a=a-1
                    b=b+1
    except:
        print("I guess that is not integer")

root3 = Tk()
window(root3)

root3.title('Goldbach Calculator')
root3.option_add("*Font","맑은고딕 30")
root3.geometry('600x400')
root3.configure(bg='lightgray')

print(p_test(17011239))

try:
    while True:
        
        root3.update()
except Exception as yee:
    print("loop break : {}".format(yee))
