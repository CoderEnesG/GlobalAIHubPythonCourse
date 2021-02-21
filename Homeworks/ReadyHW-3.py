#3. ödev
# Enes GÜNGÖR
# enesgungor.gs@gmail.com
# Quiz Notları: 90-100-100-100-100

def asal_first(number):
  for j in range(2,number):
    if number % j == 0:
      return None 
  else:
    return number, "asal_first"


def asal_second(number):
  for j in range(2,number):
    if number % j == 0:
      return None
  else:
    return number, "asal_second"

for i in range(0,1000):
  if i == 0 or i == 1:
    continue 
  elif i < 500:
    if asal_first(i) != None:
      print(asal_first(i))
  else:
    if asal_second(i) != None:
      print(asal_second(i))
