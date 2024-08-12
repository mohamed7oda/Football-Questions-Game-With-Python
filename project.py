def score(n):
    n=n+1
    return n
#first function: counting the score
def minus(n):
    n=n-1
    return n
#second function: if the answer wrong it will minus one point from the score
def percent(n,f):
    z=(n/f)*100
    return z
#third function: calculate the percentage of the right answers
def corr(n):
    print('the correct answer is ',n)
#fourth function: telling the user the correct answer
def level(c,q):
    x = input('Do you want to know your level? ')
    if x != 'yes':
        print('thx :(')
    else:
        if 30>=percent(c,q)>=0:
            print('MAGUIRE')
        elif 50>=percent(c,q)>30:
            print('JUNIOR')
        elif 70>=percent(c,q)>50:
            print('AVERAGE')
        elif 80>=percent(c,q)>70:
            print('MANAGER')
        elif 100>=percent(c,q)>80:
            print('GOAT')
#fifth function: asking the user if he want to know his level or not
def high(h,c):
    if h==c:
        print('CONGRATULATION, you have reached the high score')
#six function: telling the user if he have reached the high score or not
def milestone(q):
    if q==2:
        print('you have reached the first milestone')
        print('    coming questions are normal')
    if q==4:
        print('you have reached the second milestone')
        print('     coming questions are hard')
    if q==6:
        print('you have reached the last milestone')
        print(' there is no coming questions :[')
#seven function: telling the user where is he stand
def opinion():
    z=input('what is your opinion about the game?  ')
    file= open('7oda 2','w')
    file.write(z)
    file.close
#eight function: asking the user about his opinion on the game and save the answer in other file
def read():
    file = open('7oda','r')
    for line in file:
        print(line)
    file.close()
#nine function: print a sentence to the user
def supp():
    x=input('Right the club you support: ')
    if x != 'real madrid':
        print('UNFORTUNATELY,YOU LOST IN THE GAME BECAUSE YOU ARE NOT SUPPORTING REAL MADRID ')
    if x == 'real madrid':
        print('BRO, YOU ARE THE BEST')
#ten function: asking the user about his favorite team












h= 5
c=0
q=0
x=0
print('                         welcome to el KAWEER')
print('                          football quiz game')
print('                           -----------------')
playing = input('do you want to start? ')
if playing != 'yes':
   print('bye')
#asking the user if he want to start play or not
else:
    print('ok lets start')
print('------------------------------------------------')
print('coming questions are easy')
print('------------------------------------------------')
q=q+1
question1 = input('FIRST QUESTION: how many champions league with REAL MADRID? (a- 12 , b- 13 , c- 14 , d- 15)  ')
#asking the first question
if question1 == 'c':
 print('CORRECT')
 print('your score= ',score(x))
 c=c+1
 x=x+1
 print('you got',percent(c,q),'% of answers correct')
else:
 k='c'
 print('INCORRECT')
 corr(k)
 print('your score= ',minus(x))
 print('you got',percent(c,q),'% of answers correct')
 x=x-1
#adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('-----------------------------------------------------------------')

q=q+1
question2= input('SECOND QUESTION: how many premier league with MANCHESTER UNITED? (a- 18 , b- 20 , c- 19 , d- 21)  ')
#asking the second qustion
if question2 == 'b':
 print('CORRECT')
 print('your score=', score(x))
 c=c+1
 x=x+1
 print('you got',percent(c,q),'% of answers correct')
else:
 k = 'b'
 print('INCORRECT')
 corr(k)
 print('your score=',minus(x))
 print('you got',percent(c,q),'% of answers correct')
 x=x-1
 # adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('----------------------------------------------------------------------')
milestone(q)
#telling the user where is he stand
level(c,q)
#asking the user if he want to know his level or not
print('----------------------------------------------------------------------')


q=q+1
question3= input('THIRD QUESTION: who is the winner of BALLONDOR in 2004? (a- SHEVCHENKO , b- RONALDINHO c- HENRY , d- ZIDANE)  ')
#asking third question
if question3 == 'a':
    print('CORRECT')
    print('your score=',score(x))
    c=c+1
    x=x+1
    print('you got',percent(c,q),'% of answers correct')
else:
    k = 'a'
    print('INCORRECT')
    corr(k)
    print('your score=',minus(x))
    print('you got',percent(c,q),'% of answers correct')
    x=x-1
#adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('--------------------------------------------------------------------')


q=q+1
question4= input('FOURTH QUESTION: what is the nationality of NANI? (a- POTUGUESE , b- ITALIAN , c- FRENCH , d- BELGIAN)  ')
#asking fourth question
if question4 == 'a':
    print('CORRECT')
    print('your score=',score(x))
    c=c+1
    x=x+1
    print('you got',percent(c,q),'% of answers correct')
else:
    k = 'a'
    print('INCORRECT')
    corr(k)
    print('your score=',minus(x))
    print('you got',percent(c,q),'% of answers correct')
    x=x-1
#adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('------------------------------------------------------------------')
milestone(q)
#telling the user where is he stand
level(c,q)
#asking the user if he want to know his level or not
print('-------------------------------------------------------------------')


q=q+1
question5= input('FIFTH QUESTION: how many ballondor does ZIDANE have? (a- 3  , b- 4 , c- 2 , d- 1)  ')
#asking fifth question
if question5 == 'd':
    print('CORRECT')
    print('your score=',score(x))
    c=c+1
    x=x+1
    print('you got',percent(c,q),'% of answers correct')
else:
    k = 'd'
    print('INCORRECT')
    corr(k)
    print('your score=',minus(x))
    print('you got',percent(c,q),'% of answers correct')
    x=x-1
#adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('---------------------------------------------------------------------')


q=q+1
question6= input('SIX QUESTION: who is the EURO 2004 winning team? (a- SPAIN  , b- ITALY , c- GERMANY , d- GREECE)  ')
#asking fifth question
if question5 == 'd':
    print('CORRECT')
    print('your score=',score(x))
    c=c+1
    x=x+1
    print('you got',percent(c,q),'% of answers correct')
else:
    k = 'd'
    print('INCORRECT')
    corr(k)
    print('your score=',minus(x))
    print('you got',percent(c,q),'% of answers correct')
    x=x-1
#adding or minus one point from the score and show the user the percent
high(h,c)
#check if the user reached the high score or not
print('------------------------------------------------------------------')
milestone(q)
#telling the user where is he stand
level(c,q)
#asking the user if he want to know his level or not
print('-------------------------------------------------------------------')
print('Final score =',x )
print('Final percent=',percent(c,q),'%')
print('--------------------------------------------------------------------')


opinion()
supp()
print('---------------------------------------------------------------------')
read()
print('THX FOR PLAYING :)')


