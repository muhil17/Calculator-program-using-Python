import statistics #This package is used to find mean
def isdigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
#I am using the above code to take float value also as isdigit, so that i can get both int and float input values from user
print("-----Welcome-----")       
while(True):
 choice=input("Enter 1 to use multiple operators like (3+5*3/4) or Enter 2 to perform any one operation or Enter 0 to Exit : ")
 if(choice=='0'):
    break

 elif(choice=='1'):
    exp=input("Enter the expression with multiple operartors : ")
    print("\nThe output value for the expression is",eval(exp))
    print("Thank you for using this calculator")
    
 elif(choice=='2'):
        print("\nPlease select the operation you want to use")
        print("Addition - 1")
        print("Subtraction - 2")
        print("Multiplication - 3")
        print("Division - 4")
        print("Modulo(Remainder) - 5")
        print("To find Greatest of all numbers - 6")
        print("To find Smallest of all numbers - 7")
        print("To find Mean of all numbers - 8")
        choice1=input("Enter the proper choice : ")
        #I am not using int to get input in above code beacuse if str values are entered it shows error in the console. But i want to print it like Enter valid number in else statement.
       
        if(choice1 in ['1','2','3','4','5','6','7','8']):
            
            #n is used to get the number of inputs from the user
            #Ex - If u want to multiply 2*4*5*7 then enter 4
            n=input("Enter the number of values to perform operation. You can enter any number of values (Ex- To add 10,20,30 Enter 3) :")
            
            if n.isdigit() == True: 
              m=int(n) 
              # m-converting str to int as we have to use it in for loop range
              
              input_num=[]
              print("\nYou can enter both integer and float values")
              for i in range(m):
                print("Enter the number %d :"%(i+1),end=' ')
                num=input()
                
                #checking whether the entered value contains only int or float and then adding them to list
                if isdigit(num) == True:
                  input_num.append(float(num))
                else:
                    print("\nPlease enter a valid integer or float value")
                    break 
                
              else:
                  if choice1 == '1':
                    tot=0
                    for values in input_num:
                      tot+=values
                  elif choice1 == '2':
                     sub=1
                     for values in input_num:
                         if sub==1:
                             tot=values
                             sub=sub+1
                         else:
                             tot-=values
                  elif choice1 == '3':
                     tot=1
                     for values in input_num:
                         tot*=values
                  elif choice1 == '4':
                     div=1
                     for values in input_num:
                         if div==1:
                            tot=values
                            div=div+1
                         else:
                             tot/=values
                  elif choice1 == '5':
                     mod=1
                     for values in input_num:
                         if mod==1:
                            tot=values
                            mod=mod+1
                         else:
                             tot%=values
                  elif choice1 == '6':
                      grt=1
                      for values in input_num:
                          if grt==1:
                              tot=values
                              grt=grt+1
                          else:   
                              if tot<values:
                                  tot=values
                  elif choice1 == '7':
                      sml=1
                      for values in input_num:
                          if sml==1:
                              tot=values
                              sml=sml+1
                          else:   
                              if tot>values:
                                  tot=values    
                  elif choice1 == '8':
                      tot=statistics.mean(input_num)
                     
                  #{:g} is used to print 10 instead of 10.0
                  print("\nThe answer is {:g}".format(tot))      
                  print("Thank you for using this calculator...")
            
            else:
              print("\nPlease enter a valid integer number")
        
        else:
            print("\nPlease enter the proper operation choice given")
 else:
    print("\nPlease enter valid choice....Enter either 1 or 2")