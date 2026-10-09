for numero in range(1, 30):
  if numero % 3 == 0 and numero % 5 == 0:
    print ("FizzBuzz")
  elif numero % 5 == 0:
    print ("Buzz")
  elif numero % 3 == 0:
    print ("Fizz")
  else:
    print (numero)