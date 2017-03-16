#CS1 30 UseridPass.py
#Ismael Garrido
#This program test the accuracy of a User ID and Password entered by the user.


def intro():
    print("Welcome!, This program accesses a file and test the")
    print("given User and Passwords against the determined file")
    print()
    print("The user must enter a correct User ID and Password to gain access")
    print()
    
def getInfo():
    Username = input("Please enter your Username: ")
    Password = input("Please enter your Password: ")
    return Username, Password

def checkFile(Username, Password):
    infile = open ('UserID_passwords.txt', 'r')
    for line in infile:
        u, p = line.split()
        
        if Username == u and Password == p:
            infile.close()
            return (True)

    infile.close()
    return False
    
def main():
    intro()
    tries =  0
    while tries < 3:
        Username, Password = getInfo()
        Outcome = checkFile(Username, Password)

        if Outcome == True:
            print("Welcome Back! ")
            break

        else:
            if tries == 2:
                print (" We are sorry but the userid and/or password entered")
                print ("do not correspond with our records. Take care!")
            elif tries < 2:
                print ("Please Try Again")
            tries = tries + 1
          

main()            
        
"""
Welcome!, This program accesses a file and test the
given User and Passwords against the determined file

The user must enter a correct User ID and Password to gain access

Please enter your Username: jblack
Please enter your Password: spaniel
Welcome Back!
"""
          



          
          
    
