string1=input("Enter your string: ")# Note: Enter only [a,A,e,E,f,F,g,G,v,V]
if (string1 =='a' or string1=='A'):
    print("Average grade")
elif (string1 == 'e'or string1=='E'):
    print("Excellent")
elif (string1 == 'f'or string1=='F'):
    print("Fail")
elif (string1 == 'g'or string1=='G'):
    print("Good")
elif (string1 == 'v' or string1 =='V'):
    print("Very good")
else:
    print("Invalid string your entered")