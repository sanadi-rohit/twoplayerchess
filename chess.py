from tkinter import *
root=Tk()
root.title("CHESS")
root.configure(bg="White")

lst=[]
alpha=[]
for i in range(8):
    but=[]
    num=[]
    for j in range(8):
        num.append(j)
        but.append(j)
    alpha.append(num)
    lst.append(but)

def colorbut(i,j):
    return (i+j)%2
print(lst)
lt=[0,1,2,3,4,5,6,7]
color=['White','LightBlue']
coins=['E','H','CW','M','K','CB','H','E']
coinscolor=['Black','Red']
def coinsbut(i,j):
    coins=['E','H','C','M','K','C','H','E']
    if i<2:
        if i==0:
            return(coins[j])
        else:
            return('P')
    elif i>5:
        if i==7:
            return(coins[j])
        else:
            return('P')
    else:
        return(" ")

def coinscolorbut(i,j):
    if i<2:
        return('Black')
    elif i>5:
        return('Red')

for i in range(8):
    for j in range(8):
        alpha[i][j]=coinsbut(i,j)
print(alpha)
def refresh():
    for i in range(8):
        for j in range(8):
            lst[i][j].configure(bg=color[colorbut(i,j)])
            

q=0
r=0
buffer=""
flag=0
def flagg():
    global flag
    flag=0
    refresh()
def action(i,j):
    global flag,q,r,buffer
    flag=flag+1
    if flag%2==1:
        q=i
        r=j
        if alpha[i][j]=='E':
            buffer='E'
            for k in range(8):
                for l in range(8):
                    if k==i or l==j:
                        lst[k][l].configure(bg='yellow')
        elif alpha[i][j]=='H':
            buffer='H'
            for k in range(8):
                for l in range(8):
                    if (k==i+2 and l==j-1) or (k==i-2 and l==j-1) or (k==i+2 and l==j+1) or (k==i-2 and l==j+1):
                        lst[k][l].configure(bg='yellow')
                    elif (k==i+1 and l==j+2) or (k==i-1 and l==j+2) or (k==i+1 and l==j-2) or (k==i-1 and l==j-2):
                        lst[k][l].configure(bg='yellow')
        elif alpha[i][j]=='C':
            buffer='C'
            for k in range(8):
                if i-k>=0 and j-k>=0:
                    lst[i-k][j-k].configure(bg='yellow')
                if i+k<8 and j-k>=0:
                    lst[i+k][j-k].configure(bg='yellow')
                if i+k<8 and j+k<8:
                    lst[i+k][j+k].configure(bg='yellow')
                if i-k>=0 and j+k<8:
                    lst[i-k][j+k].configure(bg='yellow')
                               
        elif alpha[i][j]=='M':
            buffer='M'
            for k in range(8):
                if i-k>=0 and j-k>=0:
                    lst[i-k][j-k].configure(bg='yellow')
                if i+k<8 and j-k>=0:
                    lst[i+k][j-k].configure(bg='yellow')
                if i+k<8 and j+k<8:
                    lst[i+k][j+k].configure(bg='yellow')
                if i-k>=0 and j+k<8:
                    lst[i-k][j+k].configure(bg='yellow')
            for k in range(8):
                for l in range(8):
                    if k==i or l==j:
                        lst[k][l].configure(bg='yellow')
        elif alpha[i][j]=='K':
            buffer='K'
            for k in range(2):
                for l in range(2):
                    lst[abs(i-k)][abs(j-l)].configure(bg='yellow')
                    lst[abs(i+k)][abs(j+l)].configure(bg='yellow')
                    lst[abs(i-k)][abs(j+l)].configure(bg='yellow')
                    lst[abs(i+k)][abs(j-l)].configure(bg='yellow')
        elif alpha[i][j]=='P':
            buffer='P'
            if lst[i][j].cget('fg')=='Red':
                lst[i-1][j].configure(bg="yellow")
                lst[i-2][j].configure(bg="yellow")
                lst[i-1][j+1].configure(bg="yellow")
                lst[i-1][j-1].configure(bg="yellow")
            else:
                lst[i+1][j].configure(bg="yellow")
                lst[i+2][j].configure(bg="yellow")
                lst[i+1][j+1].configure(bg="yellow")
                lst[i+1][j-1].configure(bg="yellow")
        else:
            None
    else:
        if lst[i][j].cget('bg')=='yellow' and lst[q][r].cget('fg')!=lst[i][j].cget('fg'):
            if lst[i][j].cget('text')==' ' and lst[q][r].cget('text')=='P' and (q!=i and r!=j):
                flag=flag-1
            else:
                alpha[i][j]=buffer
                refresh()
                lst[q][r].configure(text="")
                lst[i][j].configure(text=buffer)
        else:
            flag=flag-1
                          
for i in range(8):
    lt[i]=Frame(root,height=6,width=20)
    lt[i].pack(side=TOP)
    for j in range(8):
        lst[i][j]=Button(lt[i],text=coinsbut(i,j),borderwidth=1,relief="groove",height=3,width=7,bg=color[colorbut(i,j)],font="retro",fg=coinscolorbut(i,j),command=lambda x=i, y=j:action(x,y))
        lst[i][j].pack(side=LEFT)
op=Frame(root,height=4,width=20)
op.pack(side=TOP)
re=Button(op,text="retake",bg="grey",font="retro",command=lambda:flagg())
re.pack(side=LEFT)
if lst[0][0].cget('height')==4:
    print('hi')

root.mainloop()
                   
