import random

print ("""hello there ! lets play hangman .there is a hidden word you should guess its letters
for  each wrong guess  you will  lose a  chance of yours .remember that you arn't allowed  to enter more than one letter  ,or  any thing which isnt considered an  alphabet""")

#a function used  to select a random word out of a list to begin the game 
def select_word ():
    word_list=["CONGRATULATIONS","WORLD","HORROR","MOVIES","SCHOOL","WIZARDS","COLLISION"]
    word=random.choice(word_list)
    #print(word)
    print("hey! the word contains",len(word),"letters  try to guess")
    return word
    #a function used to distribute the word into lettters to be later converted into dashes through which we will put  the  correct guess in its place
def showing_dashes(word):
    hidden=list(word)# used to distribute the word  into  separate letters 
    #print(hidden)
    letters_list=[]#a list through which the separeted letters  will be put
    letters_list.extend(word)
    for i in range (len(letters_list)):# a for loop that loops by the  number of letters included in the word to convert each  seprated letter into a dash 
       letters_list [i]="-"
    print(' '.join(letters_list))# to print the dashes beside each other not in the form of a list
    print()
    return letters_list
def user_input():# a function to take the input gusses from the user 
    letter=input("enter a  letter : ").upper()
    letter=letter.upper()
    return letter
def sinle_check(letters_list):#to make sure the the  user  neither inputs multiple letters nor inputs  non alphabets                         
    letter=user_input()
    alphabet="ABCDEFGHIJQKLMNOPKSTRVUWXTZ"          
    if (len(letter))!=1  :                             
        print("opps you are allowed to enter single letters only ")
        print(' '.join(letters_list)) #DASHES beside each other                  
        letter= sinle_check(letters_list)                               
    elif (letter not in alphabet):                         
        print("opps you are allowed to enter letter from A to Z")
        print(' '.join(letters_list))                  
        letter= sinle_check(letters_list) 
    return letter
def check(word,letters_list):
    guess_storage=[] # an empty list to store  all the guess history of the user
    guess_storage.extend(word) # if the user enterd the letter correctly  will be removed  out of this list
    correct_guesses=0 # a counter for the correct guesses
    chances=2*len(word) #counter for the no.of chances 
    print("you still have ",chances," chances left") 
    while correct_guesses<(len(word)) and chances > 0   : #  in order to make sure  that the user  won  or lost to  end  the game
       #print ("you guesses",correct_guesses,"letters correctly")   # has  nothing to do with this since the the dashes are regulerly replaced by letters
       letter=sinle_check(letters_list)
       for i in range(len(word)):
           if letter== word[i] and  letter in guess_storage:
               letters_list[i]=letter #a loop to check if the user input  letter is included bettween the separeted letters of the word to replace the dash with the letter
               correct_guesses+=1      #counter for  the no. of correct gusses
               #print ("you guesses",correct_guesses,"letters correctly")
               guess_storage.remove(letter)  # as long as  the user input  letter was included  between the correct guesses  it will be removed  out of our list 
       if letter not in letters_list: # if the letter wasnt one of  the  seprated letters  it  will not  be  replaced by  the dash 
            print("sorry!  try another guess ")
            chances-=1
            print("you have ",chances," chances left")
       print(' '.join(letters_list)) # to re display  the dashes  again 
       print()
    return correct_guesses 

def correctOrWrong(correct_guesses): # a function  to display a winning massege if the user enterd  all the  seprated letters in  the list
    if correct_guesses==len(word):
        print("great job you won ")
    else: 
        print("game over") # to display the loosing massege 
word=select_word()
letters_list = showing_dashes(word)
#letter=sinle_check()                                      
correct_guesses=check(word,letters_list)
correctOrWrong(correct_guesses)