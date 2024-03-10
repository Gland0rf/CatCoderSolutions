import os
import math

dir_path = "./input"
files = os.listdir(dir_path)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

amount_primes = 0

def find_primes(num):
    global amount_primes
    
    if(len(num) == 1 and is_prime(int(num))):
        amount_primes += 1
    else:
        for i in range(len(num)):
            new_num = num[:i] + num[i+1:]
            if is_prime(int(new_num)):
                find_primes(new_num)
    return amount_primes
    

for file in files:
    num = open(dir_path + "/" + file, "r").read()
    
    amount_primes = find_primes(num)
    
    f = open("output/" + file, "w")
    f.write(str(amount_primes))
    f.close()
    
    amount_primes = 0
    

    