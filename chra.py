value=input("enter your value: ")
if (value in '01234567890-1-2-3-4-5-6-7-8-9'):
    print("value is digit")
elif (value in '!@#$%^&*'):
    print("value is special character")
else:
    print("value is alphabet")