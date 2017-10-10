import random
import os

global score
score=0

#board function prints the 4X4 board
def board(l):
    """
    takes list as an arguement
    """
    print("|---|---|---|---|")
    i=0
    x=4
    while i<x:
        print("| "+str(l[i*x+0])+" | "+str(l[i*x+1])+" | "+str(l[i*x+2])+" | "+str(l[i*x+3])+" |")
        print("|---|---|---|---|")
        i+=1
#end of board() function


#start of shift() function
#shift function shifts the elements to left and add them properly
def shift(l):
    """
    takes list as an arguement
    """
    def leftmover(l):
        """
        takes list as an arguement
        """
        m=list(filter(lambda i : i!=' ',l))
        x=len(m)
        while x<4:
            m.append(' ')
            x+=1
        return m

    def adder(l):
        """
        takes list as an arguement
        """
        for count,item in enumerate(l[:3]):
            if item==' ':
                break
            else:
                if l[count]==l[count+1] and l[count]!=' ':
                    l[count]+=l[count+1]
                    global score
                    score +=l[count]
                    l[count+1]=' '
                    l=leftmover(l)
        return l



    l=leftmover(l)
    l=adder(l)
    return l
#end of shift() function

#start of check() function
#check funtion returns the a list of indices of empty spaces
def check(l):
    """
    takes list as an arguement
    """
    emptylist=[]
    for i, item in enumerate(l):
        if item==' ':
            emptylist.append(i)
    return emptylist
#end of check function

#start of fillemptylist() funtion
#fillemptylist() function fills any of the empty space with [2 or 4]
def fillemptylist(l,emptylist):
    l[random.choice(emptylist)]=random.choice(filler)
    return l
#end of fillemptylist() function

#start of move function
#move function moves the list in x direction
def move(x,l):
    """
    takes 2 arguements - a character and a list
    """
    nestlist=[]
    counter=0
    temp=list(l)

    if x=='w'or x=='W':
        while counter<4:
            nestlist.append(l[counter:16:4])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i+k*4]=item

    elif x=='s' or x=='S':
        while counter<4:
            nestlist.append(l[12+counter::-4])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i+(3-k)*4]=item

    elif x=='a' or x=='A':
        while counter<4:
            nestlist.append(l[counter*4:(counter*4)+4:1])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i*4+k]=item

    elif x=='d' or  x=='D':
        while counter<4:
            r=l[counter*4:(counter*4)+4:1]
            nestlist.append(r[::-1])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i*4+3-k]=item
    else:
        print("wrong entry : try again")


    if (x=='w' or x=='W' or x=='s' or x=='S' or x=='a' or x=='A' or x=='d' or x=='D') and temp!=l:
        emptylist=check(l)
        l=fillemptylist(l,emptylist)

    return l
#end of move() function

#start of gamestart() function
#game start function starts the game
def gamestart():
    """
    takes no arguements
    """
    print("\t \t ***2048****")
    print("==============")
    print("W - to move up")
    print("S - to move down")
    print("A - to move left")
    print("D - to move right")
    print("==============")
    while True:
            x = str(input('press Y to Start the game and N to exit:  '))
            if x== 'Y' or x=='N' or x=='y' or x=='n':
                break
            else:
                print("wrong input try again")

    if x=='Y' or x=='y':
        l=[' ']*16
        emptylist=check(l)
        l=fillemptylist(l,emptylist)
        emptylist=check(l)
        l=fillemptylist(l,emptylist)
        total=0
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("\t \t ****2048****")
            print("\t \t ============")
            print("score : {}".format(score))
            print("\n")
            board(l)
            l=move(str(input('make your move: ')),l)
            os.system('cls' if os.name == 'nt' else 'clear')
            emptylist=check(l)
            total+=1
            print(str(total)+" moves made")
            if len(emptylist)==0:
                ctemp1=list(move('w',l))
                ctemp2=list(move('s',l))
                ctemp3=list(move('a',l))
                ctemp4=list(move('d',l))
                if(ctemp1==ctemp2==ctemp3==ctemp4==l):
                    board(l)
                    print('gameover')
                    break

#end of gamestart() function
score =0
filler =[2,2,2,2,2,2,2,2,4,2]
gamestart()
