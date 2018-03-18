n1=input('Enter any number1:')
n2=input('Enter any number2:')
n3=input('Enter any number3:')

if(n1>n2) and (n1>n3):
  print('number1 is greater')
elif(n2>n1) and (n2>n3):  
  print('number2 nis greater')
elif(n1==n2) and (n2==n1):
  print('number1 and number2 are equal')
elif(n1==n3) and (n3==n1):
  print('number1 and number3 are equal')
elif(n2==n3) and (n3==n2):
  print('number2 and number3 are equal')
else:
  print('number3 is greater')
