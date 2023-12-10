import random
import array

length=int(input("Enter the length of the password: "))
digits=['0','1','2','3','4','5','6','7','8','9']
low=['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppc=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
sym=['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<']

combined_list=digits+low+uppc+sym

rand_digit=random.choice(digits)
rand_upper=random.choice(uppc)
rand_lower=random.choice(low)
rand_symbol=random.choice(sym)
temp_pass=rand_digit+rand_upper+rand_lower+rand_symbol

for x in range(length-4):
    temp_pass=temp_pass+random.choice(combined_list)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)

password=""
for x in temp_pass_list:
    password=password+x
    
print(password)