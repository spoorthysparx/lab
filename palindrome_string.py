def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return(word[1:-1])
def is_palindrome(word):
    if len(word)==0:
        print("word is not given")
    elif len(word)<=2 and word[0]==word[-1]:
        print("true")
    elif word[0]==word[-1]:
        is_palindrome(word[1:-1])
    else:
        print("false")

word=input("Enter a string:")
is_palindrome(word)
