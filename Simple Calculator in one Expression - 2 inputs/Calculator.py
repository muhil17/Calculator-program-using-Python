import re
while True:
 x=input("Enter the expression (Ex:2+3) (+,-,*,/,%) (0 for Exit) : ")
 y=re.split('(\D)',x)
 if(int(y[0])==0):
    break
 else:
  if(y[1]=='+'):
   z=int(y[0])+int(y[2])
   print(z)
  elif(y[1]=='-'):
   z=int(y[0])-int(y[2])
   print(z)
  elif(y[1]=='*'):
   z=int(y[0])*int(y[2])
   print(z)
  elif(y[1]=='/'):
   z=int(y[0])/int(y[2])
   print(z)
  elif(y[1]=='%'):
   z=int(y[0])%int(y[2])
   print(z)   
  else:
   print("Invalid Operator")    
