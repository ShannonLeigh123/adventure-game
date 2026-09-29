# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 05:56:48 2024
Simple Fun Adventure Game
@author: Shannon
"""

nick_name = input('Please enter your game name: ')
print(f"Welcome to the jungle, {nick_name}!")
print('(answers can be the whole word or just the first letter)')

reply = input('''You are stumbling through the jungle and can go Left or Right.
Do you want to go left or right? ''').lower()

if reply in ['left', 'l']:
    reply = input('You fall into a crocodile-infested river, and you cannot swim. Do you sink or float? ').lower()
    if reply in ['float','f']:
        print('You floated down the river right into a hippo!')
    elif reply in ['sink','s']:
        print('You sank right down into the mouth of a giant crocodile!')
    else:
        print('You are screwed all around, sucka!')

elif reply in ['right','r']:
    reply = input('''You've come to a broken, wobbly bridge.
Do you dare try and cross or do you sneak back and have your tea and crumpets?
Type cross or back: ''').lower()

    if reply in ['cross','c']:
        print("You are so chucked. There is a hungry, mad lion waiting for you. Sad face.")
    elif reply in ['back','b']:
        reply = input('You back away from the bridge and meet a stranger. Do you knock them over (yes/no)? ').lower()
        if reply in ['yes','y']:
            print('You talk to the stranger and they throw you over the bridge anyway!')
        elif reply in ['no','n']:
            print('You and the stranger both end up jumping off the bridge to escape the even madder, more humgry lioness')
        else:
            print('Not what was asked, try something else!')
    else:
        print('Not a valid answer')
else:
    print("That choice doesn't' exist!")

print("The struggle is real....")



