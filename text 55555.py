
def game():
    secretword = 'folabi'
    i =0
    answer=''
    '''print('welcome stranger, Trust you are good')'''
    '''name=input('what will you like me to call you?  ')'''
    print(namer + ' lets get it going')
    question1=input('i am a man with 5 legs two head and one big hand, WHAT AM I?   ')


    if question1 != secretword:
        print('try again')
        question1=input('i am a man with 5 legs two head and one big hand, WHat am i?  ')
        i = i + 1
        if i == 2:
            print ('your game is over')
            
    else:
        print('you won')
    print('thanks for coming')
def game2():

    i = 0
    
    print('welcome stranger, this is a CA test to know what you know')
    name=input('Who is the presnt president of Nigeria? (a) Yaradua (b)Goodluck (c)Buari  ' )
    if name == 'c':
        i=i+1
    else:
        i=i+0
    name2=input('when is the next election? (a)2019 (b) 2018 (c) 2017  '  )
    if name2 == 'a':
        i = i+1
    else:
        i=i+0
    name3=input('where is the capital of nigeria? (a) kokodome (b)abuja (c) Ibadan   ')
    if name3 == 'b':
        i=i+1
    else:
        i=i+0
    print('weldone your scores is ' +str(i))
question='questions'
question2='question'

namer=input('welcome new users, what will you like me to call you ? ')
print()
print('welcome ' + namer + ' !')
query=input('which of the game will you like to play ? ' + 'pls choose between QUESTIONS and GAME ')
if query == question2:
    game2()
if query != question2:
    print(game())
    
else:
    print('sorry you entered and inValid command')


