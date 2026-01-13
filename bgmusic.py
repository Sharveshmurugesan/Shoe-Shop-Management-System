import pygame as p
import time as t
p.init()
p.display.set_caption('SHOE SALES')
a=p.display.set_mode((700,600))
bs=p.image.load('C:\\Users\\sharv\\Downloads\\Adshoe1.jpg')
a.blit(bs,(50,60))
p.display.update()
t.sleep(1)

p.init()
p.mixer.music.load('C:\\Users\\sharv\\Music\\kaththi-theme-4255.mp3')
p.mixer.music.play()
t.sleep(8)
p.quit()

print('                                           SSS SHOE SHOP                                  ')

def s1():
    v='sharvesh'
    j=1234
    a=input('Enter the username: ')
    b=int(input('Enter the password: '))
    if a==v:
        if b==j:
            print("Login successfully")
        else:
            print('Password incorrect')
            s1()
    else:
        print('user name incorrect')
        s1()

s1()

def choose_brands():
