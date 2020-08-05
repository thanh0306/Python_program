def testme(userinput):
    if len(userinput) > 6:
        if all(char.isdigit() for char in userinput) == True:
            return False
        elif any(not char.isalnum() for char in userinput) == True:
            return False
        elif all(char.isalpha() for char in userinput) == True:
            return False
        elif any(char.isdigit() for char in userinput) == True:
            return True
    else:
        return False