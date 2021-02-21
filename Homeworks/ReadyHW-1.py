#1. ÖDEV
# Enes GÜNGÖR
# enesgungor.gs@gmail.com

import random

primeNumbers=[]

lower = 2
upper = 100

for num in range(lower, upper + 1):
  
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primeNumbers.append(num) #asal sayıları seçerim


i=0
a=0
matrixNumbers = [],[],[] 
while i<9:
  randomNum = random.choice(primeNumbers)
  if randomNum not in matrixNumbers[0] and randomNum not in matrixNumbers[1] and randomNum not in matrixNumbers[2] :   
    matrixNumbers[a].append(randomNum)
  else:
    continue  
  i += 1
	# i 1 artacak ve 9 sayıya sahip olacağım
  if i%3==0:
	# listede 3 sayı olmasını sağlar
    print(matrixNumbers[a])
    a+=1
