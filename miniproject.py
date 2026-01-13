import pygame as p
import time as t
import random
p.init()
a=p.display.set_mode((700,600))
bs=p.image.load('C:\\Users\\sharv\\Downloads\\Adshoe1.jpg')
a.blit(bs,(50,60))
p.display.update()
t.sleep(1)

p.init()
p.mixer.music.load("C:\\Users\\sharv\\OneDrive\\Music\\kaththi-theme-4255.mp3")
p.mixer.music.play()
t.sleep(8)
p.quit()

print('                                                     SSS SHOE SHOP')

def s1():
    v='sharvesh'
    j=1234
    a=input('Enter the username: ')
    b=int(input('Enter the password: '))
    if a==v:
        if b==j:
            print("Login successful")
        else:
            print('Password incorrect')
            s1()
    else:
        print('user name incorrect')
        s1()

s1()

def payment_method():
    print('                                            Payment choice')
    print('1.Debit card\n2.Google pay\n3.Cash on delivery')
    s1 = int(input('Select payment method: '))
    if s1==1:
        print('                                       Debit card details')
        a=input('Enter your name as per your debit card: ')
        p=int(input('Enter your pin: '))
        o=int(input('Enter OTP: '))
        while p==o:
            print('Invalid otp')
            print('Re-Enter your OTP: ')
            payment_method()
        print('Payment processing...')
        t.sleep(5)
        print('Payment successful')
        print('Your order has been placed')
        print('Delivery within the next 4 business days')
        t.sleep(3)
        print('                                     Thank you for shopping with us visit again...')

    elif s1 == 2:
        print('                                       Google pay details')
        a = input('Enter your UPI Id: ')
        p = int(input('Enter your pin: '))
        n = input('Enter your name: ')
        a1 = input('Enter your address: ')
        mn = int(input('Enter your mobile number: '))
        print('Payment processing...')
        t.sleep(5)
        print('Payment successful')
        print('Your order has been placed')
        print('Delivery within the next 4 business days')
        t.sleep(3)
        print('                                     Thank you for shopping with us visit again...')
    elif s1==3:
        print('                                        Cash on delivery')
        n=input('Enter your name: ')
        a=input('Enter your address: ')
        mn=int(input('Enter your mobile number: '))
        print('Your order has been placed')
        print('Delivery within the next 4 business days')
        t.sleep(3)
        print('                                     Thank you for shopping with us visit again...')
    else:
        print('Please select correct option')
        payment_method()


def choose_brands():
    print('                                          Available brands:')
    print('1.Adidas\n2.Puma\n3.One8\n4.Nike')
    a=int(input('Select the brand: '))
    if a==1:
        print('                                           Adidas')
        p.init()
        a = p.display.set_mode((500, 400))
        bs = p.image.load('C:\\Users\\sharv\\Downloads\\adidas1.jpg')
        a.blit(bs, (150, 50))
        p.display.update()
        t.sleep(3)
        p.quit()
        t.sleep(3)
        print("You can get this model in black or white color")
    elif a==2:
        print('                                           Puma')
        p.init()
        a=p.display.set_mode((600, 500))
        bs=p.image.load('C:\\Users\\sharv\\Downloads\\puma1.jpg')
        a.blit(bs,(40, 35))
        p.display.update()
        t.sleep(3)
        p.quit()
        t.sleep(3)
        print("You can get this model in black or white color")
    elif a==3:
        print('                                           One8')
        p.init()
        a=p.display.set_mode((600, 500))
        bs=p.image.load('C:\\Users\\sharv\\Downloads\\one8.jpg')
        a.blit(bs, (70, 60))
        p.display.update()
        t.sleep(3)
        p.quit()
        t.sleep(3)
        print("You can get this model in black or white color")
    elif a==4:
        print('                                           Nike')
        p.init()
        a=p.display.set_mode((600,500))
        bs=p.image.load('C:\\Users\\sharv\\Downloads\\nike3.jpg')
        a.blit(bs, (90, 70))
        p.display.update()
        t.sleep(3)
        p.quit()
        t.sleep(3)
        print("You can get this model in black or white color")
    else:
        print('Please select the correct option')
        choose_brands()
choose_brands()


def choose_color():
    print('1.White\n2.Black')
    a=int(input('Select your color: '))
    if a==1:
        print("You have selected the color: White.")
    elif a== 2:
        print("You have selected the color: Black.")
    else:
        print("Invalid choice. Please select 1 for White or 2 for Black.")
        choose_color()
choose_color()


def size():
    print('8\n9\n10')
    a=int(input('Select your size or Enter the size you needed: '))
    if a==8:
        prices=random.randint(2000, 3200)
        print('The price of your product is:')
        print(prices)
        delivery_charge = 40
        total_amount = prices + delivery_charge
        print('The delivery charge for your order is ₹40:')
        print(total_amount)
        payment_method()
    elif a==9:
        prices=random.randint(1400, 2000)
        print('The price of your product is:')
        print(prices)
        delivery_charge = 40
        total_amount = prices + delivery_charge
        print('The delivery charge for your order is ₹40:')
        print(total_amount)
        payment_method()
    elif a==10:
        prices=random.randint(3000, 4500)
        print('The price of your product is:')
        print(prices)
        delivery_charge = 40
        total_amount = prices + delivery_charge
        print('The delivery charge for your order is ₹40:')
        print(total_amount)
        payment_method()
    elif a<=15:
        prices=random.randint(1400, 2000)
        print('The price of your product is:')
        print(prices)
        delivery_charge = 40
        total_amount = prices + delivery_charge
        print('The delivery charge for your order is ₹40:')
        print(total_amount)
        payment_method()
    else:
        print('Please enter valuable size')
        size()
size()


p.init()
a=p.display.set_mode((600,500))
bs=p.image.load('C:\\Users\\sharv\\Downloads\\thankyou.jpg')
a.blit(bs,(60,60))
p.display.update()
t.sleep(5)
p.quit()
















