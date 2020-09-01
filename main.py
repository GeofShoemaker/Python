print("Give me three numbers")
num1 = int(input("1.) "))
num2 = int(input("2.) "))
num3 = int(input("3.) "))
choice = input("GCF or LCM? ")
if(choice.lower()=="gcf"):
  gc = min(num1,min(num2,num3))
  while gc>0:
    if(num1%gc==0 and num2%gc==0 and num3%gc==0):
      break
    gc-=1
  print(f"The GCF is: {gc}.");
elif(choice.lower()=="lcm"):
  mSum = num1*num2*num3
  lc = max(num1,max(num2,num3))
  while(lc <=mSum):
    if(lc%num1==0 and lc%num2==0 and lc%num3==0):
      break
    lc+=1
  print(f"The LCM is: {lc}.")
else:    
  print("That is not a choice.")        