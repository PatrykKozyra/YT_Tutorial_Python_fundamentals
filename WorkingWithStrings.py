
#print("Cracow\nUniversity")
#print("Cracow\"University")  #quotes will be printed out
#print("Cracow", "\ " "University") #will print backslash

phrase = "Cracow University"
#print(phrase + " is cool")

#print(phrase.lower())  #lowercase
#print(phrase.upper())  #uppercase

# print(phrase.isupper())  #false, because it is not entirely uppercase
# print(phrase.upper().isupper())  #true, because it was changed to uppercase before isupper

# print(len(phrase))  #check lenght of string
# print(phrase[0])  #first charachter
# print(phrase[-1]) #last character
# print(phrase.index("Uni"))  #check position, where it starts
# print(phrase.replace("University","School"))   #replace words/letters with other once