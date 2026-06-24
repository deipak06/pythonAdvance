
# Print numbers 1-100, but "Fizz" for multiples of 3, 
# "Buzz" for multiples of 5, "FizzBuzz" for both 
# (classic, but actually do it yourself, 
# don't look up the answer)

for i in range(0,100):
    if i%3 == 0 and i%5 ==0:
         print("FizzBuzz")
    elif i%3==0:
         print("Fizz")
    elif i%5==0:
         print("Buzz")
    else: print (f"{i}")