alphabet=input("enter a alphabet")
num=int(input("enter a number"))
num2=int(input("enter another num"))
special_char=input("enter a special character")
if alphabet >="A"and alphabet <="Z":
    if num>=0 and num<=9:
        if num2>=0 and num2<=9:
            if special_char== "@" or special_char=="$" or special_char == "&":
                print("its a strong password")
            else:
                print("enter a special charecter")
        else:
            print("enter another no")
    else:
        print("enter proper number")
else:
    print("enter any capital alphabet")
# password="N98@"
# alphabet=input("enter a alphabet")
# num=input("enter a number")
# special_char=input("enter a special character")
# if alphabet in password:
#     print("wait its in prosess")
#     if num in password:
#         print("one more step to login")
#         if special_char in password:
#             print("its a strong password")
#         else:
#             print("check the password once again")
#     else:
#         print("check the password once again")
# else:
#     print("check the password once again")