print("Give me three numbers\nDon't try any funny business or you're gonna restart ;)")
while True:
  try:
    num1 = int(input("1.) "))
    num2 = int(input("2.) "))
    num3 = int(input("3.) "))
    choice = input("GCF or LCM? ")
    if(choice.lower()=="gcf"):
      gc = min(num1,min(num2,num3))
      while gc>0 and not(num1%gc==0 and num2%gc==0 and num3%gc==0):
        gc-=1
      print(f"The GCF is: {gc}")
      break
    elif(choice.lower()=="lcm"):
      lc = max(num1,max(num2,num3))
      while lc<=num1*num2*num3 and not(lc%num1==0 and lc%num2==0 and lc%num3==0):
        lc+=1
      print(f"The LCM is: {lc}")
      break
    else: FU = 42/0    
  except:
    print("That's not a valid input, try again. ;)")
