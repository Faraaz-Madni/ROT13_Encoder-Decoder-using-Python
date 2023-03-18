string = "uggcf://lbhgh.or/HUvqp7aR-vZ"                                    #String to either convert or decode via ROT13

print(string)
solvedArray = []
for i in string:
    i = ord(i)
    if (i>= 97 and i <= 122):                                               #If ASCII letter is lowercase - ASCII Value from 97 till 122 
        ogAns = chr(i)
        rot13_uni = int(i+13)
        print("rot13_uni is: ", rot13_uni)
        if (rot13_uni > 122):
            ans = chr(i-13)
            print("-------")
            print("13 is being deducted")
            print("Original answer:", ogAns, " Changed answer: ", ans)
            print("Original unicode value=", i)
            print("Changed unicode value=", i-13)
            solvedArray.append(ans)
        else:
            ans = chr(i+13)
            print("-------")
            print("13 is being added")
            print("Original answer:", ogAns, " Changed answer: ", ans)
            print("Original unicode value=", i)
            print("Changed unicode value=", i+13)
            solvedArray.append(ans)
    elif (i>= 65 and i <= 90):                                              #or If ASCII letter is uppercase - ASCII Value from 65 till 90.
            ogAns = chr(i)
            rot13_uni = int(i+13)
            print("rot13_uni is: ", rot13_uni)
            if (rot13_uni > 90):
                ans = chr(i-13)
                print("-------")
                print("13 is being deducted")
                print("Original answer:", ogAns, " Changed answer: ", ans)
                print("Original unicode value=", i)
                print("Changed unicode value=", i-13)
                solvedArray.append(ans)
            else:
                ans = chr(i+13)
                print("-------")
                print("13 is being added")
                print("Original answer:", ogAns, " Changed answer: ", ans)
                print("Original unicode value=", i)
                print("Changed unicode value=", i+13)
                solvedArray.append(ans)
    else:         
        ans=chr(i)
        print("-------")
        print("SPECIAL CHARACTER: ", ans)                                   #In case of any other characters.
        solvedArray.append(ans)

#Convert Array to string
solvedString = "".join([str(i) for i in solvedArray])

print("The solved string is:",solvedString)
