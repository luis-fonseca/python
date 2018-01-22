def prime(x):  
  for number in range(2, x):
    if x % number == 0:
      print "not prime"
      return False      
  else:
    print "prime"  
    return True
      
def is_prime(x):
  
  if x >= 2 and prime(x):
    return True
  
  return False