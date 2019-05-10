def check_palindrome(word):
    rev=word[::-1]
    if(word==rev):
        return True
    else:
        return False
status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
