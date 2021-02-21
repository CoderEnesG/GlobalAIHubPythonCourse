#3. ödev
# Enes GÜNGÖR
# enesgungor.gs@gmail.com

def prime_first(number):
  for j in range(2,number):
    if number % j == 0:
      return None 
  else:
    return number, "prime_first"


def prime_second(number):
  for j in range(2,number):
    if number % j == 0:
      return None
  else:
    return number, "prime_second"

for i in range(0,1000):
  if i == 0 or i == 1:
    continue 
  elif i < 500:
    if prime_first(i) != None:
      print(prime_first(i))
  else:
    if prime_second(i) != None:
      print(prime_second(i))
