############
# Passgen #
# Public Code, For use in multitools or whatever yah want #
# I have some more stuff lmk if you need anything  Discord (ClamLq#000)1   #
# SAVE AS main.py or it wont work #
# or edit line 58 'import main' and change it to 'import filename'#
############
import random
import time
import os
import sys
import string
 
print("""
[Lewd V1.0] Welcome To Pass Gen, Public Script \n[Params: 13 Characters  Capitols, Numbers, Symbols. \nall passwords saved to Pass.txt\nin the same folder as the script]
    """)
length = 13
chars = string.ascii_letters + string.digits + "!@$%^&*()" 
random.seed = (os.urandom(1024))
 
a = print(''.join(random.choice(chars) for i in range(length)))
time.sleep(1)
 
b = print(''.join(random.choice(chars) for i in range(length)))
time.sleep(1)
 
c = print(''.join(random.choice(chars) for i in range(length)))
time.sleep(1)
 
d = print(''.join(random.choice(chars) for i in range(length)))
time.sleep(1)
 
e = print(''.join(random.choice(chars) for i in range(length)))
time.sleep(1)
 
f = file.open("pass.txt", "a")
f.write("{Password Log round of Passgen By ClamLq} ")
f.write("[PassGen :)]")
f.write(a)
f.write("[PassGen :)]")
f.write(b)
f.write("[PassGen :)]")
f.write(c)
f.write("[PassGen :)]")
f.write(d)
f.write("[PassGen :)]")
f.write(e)
f.close()
 
a = input("[~] Password Generated, Would you like to generate more? [y/n]: ")
if a == 'n':
    os.system('cls')
    print("[:)] Have A Good Day [~]")
    time.sleep(2)
    sys.exit()
   
if a == 'y':
    import main
 
if a != 'y' or 'n':
    os.system('cls')
    print("[\] Invalid Params [\]")
    time.sleep(1)
    sys.exit(1)
    ##################################################
##################Discord: ClamLq#0001    ##############
    ##################################################
# pls keep credit :) #
