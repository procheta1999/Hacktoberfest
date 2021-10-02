a=int(input("Enter a number whose factorial you want to calculate"))
b=1
if a==0:
  print("The factorial of ", a , " is ",b) 
elif a<0:
  print("Please enter a number greater than 0")
else:
  for i in range(a):
    b*=(a+1)
  print("The factorial of ",a," is ",b)
