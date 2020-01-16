import tkinter as t
import threading
import time


def callmethod():
    h,m,s=0,1,59    # change time 2,59,59 2 hour 59 minute 59 second
    while h<=2:
        if s<0:
            s=59
            m-=1
            if m<0:
                m=59
                h-=1
                if h<0:
                    root.destroy()
        time.sleep(1)
        
        rtime["text"]=h,":",m,":",s  #assing value at every second
        root.update() #update at every second
       
        s-=1 #deduce a 1 second by second

def one():
    t.Label(root,text="Click").pack()

root=t.Tk()
root.title("Timer")
root.geometry("200x200")

rtime=t.Label() #remain time
rtime.pack()

btn=t.Button(root,text="Button",width=10,height=3,command=one)
btn.pack()
    
t1=threading.Thread(target=callmethod)
t1.start()
#callmethod()
root.mainloop()
print("saaddsd")

