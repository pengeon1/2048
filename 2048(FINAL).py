import random
from tkinter import *
from tkinter import messagebox

grid_real = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

grid = [x[:] for x in grid_real]

def add2():
    r = random.randint(0,3)
    c = random.randint(0,3)
    while grid_real[r][c]!=0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    grid_real[r][c]=2

#adding the intial 2
add2()
    
def down():
    global grid_real
    for i in range(4):
        for j in range(4):
            grid[i][j]=grid_real[i][j]
    for times in range(4):
        for c in range(3,-1,-1):
            for r in range(3,-1,-1):
                if r==0:
                    break
                if grid[r][c]==0:
                    grid[r][c]=grid[r-1][c]
                    grid[r-1][c]=0
    #summing up        
    for c in range(4):
        #bottom 2 add up            
        if grid[3][c]==grid[2][c]:
            grid[3][c]=grid[3][c]*2 
            #top 2 add up                
            if grid[1][c]==grid[0][c]:
                grid[2][c]=grid[1][c]*2
                grid[1][c]=0
                grid[0][c]=0
            #top 2 dont add up                
            else:
                grid[2][c]=grid[1][c]
                grid[1][c]=grid[0][c]
                grid[0][c]=0
        #bottom 2 dont add up            
        else:
            #middle add up                
            if grid[2][c]==grid[1][c]:
                grid[2][c]=grid[2][c]*2
                grid[1][c]=grid[0][c]
                grid[0][c]=0
            #top 2 add up
            else:
                if grid[1][c]==grid[0][c]:
                    grid[1][c]=grid[1][c]*2
                    grid[0][c]=0
                else:
                    pass

def up():
    global grid_real
    for i in range(4):
        for j in range(4):
            grid[i][j]=grid_real[i][j]
    for times in range(4):
        for c in range(3,-1,-1):
            for r in range(4):
                if r==3:
                    break
                if grid[r][c]==0:
                    grid[r][c]=grid[r+1][c]
                    grid[r+1][c]=0
    #summing up        
    for c in range(4):
        #top 2 add up            
        if grid[0][c]==grid[1][c]:
            grid[0][c]=grid[0][c]*2 
            #bottom 2 add up                
            if grid[2][c]==grid[3][c]:
                grid[1][c]=grid[2][c]*2
                grid[2][c]=0
                grid[3][c]=0
            #bottom 2 dont add up                
            else:
                grid[1][c]=grid[2][c]
                grid[2][c]=grid[3][c]
                grid[3][c]=0
        #top 2 dont add up            
        else:
            #middle add up                
            if grid[1][c]==grid[2][c]:
                grid[1][c]=grid[1][c]*2
                grid[2][c]=grid[3][c]
                grid[3][c]=0
            #bottom 2 add up
            else:
                if grid[2][c]==grid[3][c]:
                    grid[2][c]=grid[2][c]*2
                    grid[3][c]=0
                else:
                    pass

def left():
    global grid_real
    for i in range(4):
        for j in range(4):
            grid[i][j]=grid_real[i][j]
    for times in range(4):
        for r in range(4):
            for c in range(4):
                if c==3:
                    break
                if grid[r][c]==0:
                    grid[r][c]=grid[r][c+1]
                    grid[r][c+1]=0
    #summing up        
    for r in range(4):
        #left 2 add up            
        if grid[r][0]==grid[r][1]:
            grid[r][0]=grid[r][0]*2 
            #right 2 add up                
            if grid[r][2]==grid[r][3]:
                grid[r][1]=grid[r][2]*2
                grid[r][2]=0
                grid[r][3]=0
            #right 2 dont add up                
            else:
                grid[r][1]=grid[r][2]
                grid[r][2]=grid[r][3]
                grid[r][3]=0
        #left 2 dont add up            
        else:
            #middle add up                
            if grid[r][1]==grid[r][2]:
                grid[r][1]=grid[r][1]*2
                grid[r][2]=grid[r][3]
                grid[r][3]=0
            #right 2 add up
            else:
                if grid[r][2]==grid[r][3]:
                    grid[r][2]=grid[r][2]*2
                    grid[r][3]=0
                else:
                    pass

def right():
    global grid_real
    for i in range(4):
        for j in range(4):
            grid[i][j]=grid_real[i][j]
    for times in range(4):
        for r in range(4):
            for c in range(3,-1,-1):
                if c==0:
                    break
                if grid[r][c]==0:
                    grid[r][c]=grid[r][c-1]
                    grid[r][c-1]=0
    #summing up        
    for r in range(4):
        #right 2 add up            
        if grid[r][3]==grid[r][2]:
            grid[r][3]=grid[r][3]*2 
            #left 2 add up                
            if grid[r][1]==grid[r][0]:
                grid[r][2]=grid[r][1]*2
                grid[r][1]=0
                grid[r][0]=0
            #left 2 dont add up                
            else:
                grid[r][2]=grid[r][1]
                grid[r][1]=grid[r][0]
                grid[r][0]=0
        #right 2 dont add up            
        else:
            #middle add up                
            if grid[r][2]==grid[r][1]:
                grid[r][2]=grid[r][2]*2
                grid[r][1]=grid[r][0]
                grid[r][0]=0
            #left 2 add up
            else:
                if grid[r][1]==grid[r][0]:
                    grid[r][1]=grid[r][1]*2
                    grid[r][0]=0
                else:
                    pass
    
def game(event):
    global grid_real,grid
    key_pressed=event.keysym
    if key_pressed=='Down':
        down()
    if key_pressed=='Up':
        up()
    if key_pressed=='Left':
        left()
    if key_pressed=='Right':
        right()
    if grid!=grid_real:
        grid_real = [x[:] for x in grid]
        add2()
        grid = [x[:] for x in grid_real]
        
def update():
    for x in range(4):
        for y in range(4):
            L=grp[x][y]
            if grid_real[x][y]==2:
                L.configure(image=photo2)
            if grid_real[x][y]==4:
                L.configure(image=photo4)
            if grid_real[x][y]==8:
                L.configure(image=photo8)
            if grid_real[x][y]==16:
                L.configure(image=photo16)
            if grid_real[x][y]==32:
                L.configure(image=photo32)
            if grid_real[x][y]==64:
                L.configure(image=photo64)
            if grid_real[x][y]==128:
                L.configure(image=photo128)
            if grid_real[x][y]==256:
                L.configure(image=photo256)
            if grid_real[x][y]==512:
                L.configure(image=photo512)
            if grid_real[x][y]==1024:
                L.configure(image=photo1024)
            if grid_real[x][y]==2048:
                L.configure(image=photo2048)
            if grid_real[x][y]==0:
                L.configure(image=photo)
               
#assigning the first screen

root=Tk()
root.title('2048 - Made by Piyush Mishra')
root.config(bg='#B7AF9C')

photo2 = PhotoImage(file="./a.png")
photo4 = PhotoImage(file='./b.png')
photo8 = PhotoImage(file='./c.png')
photo16 = PhotoImage(file='./d.png')
photo32 = PhotoImage(file='./e.png')
photo64 = PhotoImage(file='./f.png')
photo128 = PhotoImage(file='./g.png')
photo256 = PhotoImage(file='./h.png')
photo512 = PhotoImage(file='./i.png')
photo1024 = PhotoImage(file='./j.png')
photo2048 = PhotoImage(file='./k.png')
photo = PhotoImage(file='./l.png')

grp=[['A1','A2','A3','A4'],
     ['B1','B2','B3','B4'],
     ['C1','C2','C3','C4'],
     ['D1','D2','D3','D4']]

for i in range(4):
    for j in range(4):
        if grid_real[i][j]==0:
            grp[i][j]=Label(root,image=photo,bd=-2)
            grp[i][j].grid(row=i,column=j)
        elif grid_real[i][j]==2:
            grp[i][j]=Label(root,image=photo2,bd=-2)
            grp[i][j].grid(row=i,column=j)

def run_game():
    global grid,grid_real
    end=0
    flag=0
    while end==0:
        grid = [x[:] for x in grid_real]
        root.bind('<Key>', game)
        update()
        root.update()
        flag*=2
        for i in grid_real:
            for j in i:
                if j==2048 and flag!=2:
                    flag=1
        if flag==2:
            messagebox.showinfo("Congrats","You Win!")
            root.after(500,lambda:root.destroy())
            root.mainloop()
            end=1
        #checking if no more moves left
        flag1=0
        right()
        if grid==grid_real:
            flag1+=1
            grid_real=[x[:] for x in grid]
        left()
        if grid==grid_real:
            flag1+=1
            grid_real=[x[:] for x in grid]
        down()
        if grid==grid_real:
            flag1+=1
            grid_real=[x[:] for x in grid]
        up()
        if grid==grid_real:
            flag1+=1
            grid_real=[x[:] for x in grid]
        if flag1==4:
            root.after(100)
            messagebox.showinfo("You Lose","No more moves left!")
            root.after(500,lambda:root.destroy())
            root.mainloop()
            end=1
run_game()
exit()
