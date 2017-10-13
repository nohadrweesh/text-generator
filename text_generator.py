import string,random
vowels="aeiouy"
constants="bcdfghjklmnpqrstvwxz"
letters=string.ascii_lowercase
letter_input_1=input("What letter do you want? Enter 'v' for vowels , 'c' for constants,'l' for any letter  ")
letter_input_2=input("What letter do you want? Enter 'v' for vowels , 'c' for constants,'l' for any letter  ")
letter_input_3=input("What letter do you want? Enter 'v' for vowels , 'c' for constants,'l' for any letter  ")
def chooseLetter(char):
    if(char=='v'):
        retChar=random.choice(vowels)
    elif(char=='c'):
        retChar=random.choice(constants)
    elif(char=='l'):
        retChar=random.choice(letters)
    else:
         retChar=char
    return retChar

        
def generator():
    letter1=chooseLetter(letter_input_1)
    letter2=chooseLetter(letter_input_2)
    letter3=chooseLetter(letter_input_3)
    
    word=letter1+letter2+letter3
    return(word)
print(generator())
    