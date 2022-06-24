'''Write a function called user_name that generates a username from
the user’s email. The code should ask the user to input an email and
the code should return everything before the @ sign as their user
name. For example, if someone enters ben@gmail.com, the code
should return ben as their user name.'''



def user_name(username):
    if not '@' in username:
        print("[-]Enter a Valid email!!") # check to make Sure the username entered is correct
    else:
        return username.split("@")[0]# the .split() function returns a list of substrings, in this case, seperated by the @ delimeter
                    # I used [0] index to access the first element in the list which is the username 



# lets try to call the function and see what happens 

if __name__ == '__main__':
    print(user_name(str(input("Enter your username here :  "))))
