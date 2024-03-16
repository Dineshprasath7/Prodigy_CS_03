passwd = input("Enter password: ")
x=len(passwd)
print(x)
has_upper = False
has_num = False
has_lower = False
has_special_char= False
len_check = False
for char in passwd:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_num = True
    elif char.islower():
        has_lower = True
    elif (not char.isalnum()):
        has_special_char = True
    elif (x > 8):
        len_check = True
print(has_lower )
print(has_num)
print(has_special_char)
print(len_check)
print(has_upper)
if(len_check and has_lower and has_num and has_special_char and has_upper):
    print("It's a strong password")

else:
    print("You gotta change your password.")
    
