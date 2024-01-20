#######//////////////////////########
                              ## 1 ##
'''
 Below are a set of scores that students have received in the past semester. 
 Write code to determine how many are 90 or above and assign that result to the value a_scores
'''
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74\
     83 88 80 86 85 70 90 100"
score_list = scores.split( )   # split (" ")
a_scores = 0
print (score_list)
for score in score_list:
    x= int (score)
    if x >= 90 :
       a_scores = a_scores +1
print (a_scores)   

#######//////////////////////########
                                 ## 2 ##
""" 
Write code that uses the string stored in org and creates an acronym 
which is assigned to the variable acro. Only the first letter of each word should be used
each letter in the acronym should be a capital letter,
 and there should be nothing to separate the letters of the acronym.
Words that should not be included in the acronym are stored in the list stopwords.
For example,if org was assigned the string “hello to world”
 then the resulting acronym should be “HW”. 
"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
or_list = org.split()
#print (or_list)
for or1 in or_list :
    if or1 not in stopwords :
        #print (or1[0])
        acro = acro + or1[0].upper()
print (acro)

#######//////////////////////
                      ## 3 ##
""" 
Write code that uses the string stored in sent and creates an acronym
 which is assigned to the variable acro.
 The first two letters of each word should be used,
 each letter in the acronym should be a capital letter,
 and each element of the acronym should be separated by a “. ” (dot and space).
 Words that should not be included in the acronym are stored in the list stopwords.
 For example, if sent was assigned the string “height and ewok wonder” 
then the resulting acronym should be “HE. EW. WO”. 
"""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
or_list = sent.split()
#print (or_list)
for or1 in or_list :
    if or1 not in stopwords :
        #print (or1[0])
        acro = acro + or1[0].upper()+or1[1].upper()+". "
# rem >>  string immutable so we cant change it
acro = acro[:-2]          #remove end dot to mate task
print (acro)

#######//////////////////////########
                           ## 4 ##
""" 
A palindrome is a phrase that, if reversed,would read the exact same. 
Write code that checks if p_phrase is a palindrome by reversing it 
and then checking if the reversed version is equal to the original.
 Assign the reversed version of p_phrase to the variable r_phrase
 so that we can check your work. 
"""
# check with word :
p_phrase = "was it a car or a cat I saw"
#p_ = p_phrase .split("")    ## not valid 
p_phrase_list = []
for chars in p_phrase :
    p_phrase_list.append(chars)
print (p_phrase_list)
p_phrase_list.reverse()
print(p_phrase_list)
r_phrase = "".join(p_phrase_list)
print (r_phrase)
if p_phrase != r_phrase :
    print ("p_phrase is a non palindrome ")

## check with char :
p_phrase = "was it a car or a cat I saw"
p_ = []
for i in p_phrase :
    p_.append(i)
p_.reverse()
r_phrase = ""
for i in p_ :
    r_phrase = r_phrase + i
print (r_phrase)

#######//////////////////////########
## 5 ##
# Provided is a list of data about a store’s inventory where each item in the list
#  represents the name of an item, how much is in stock, 
# and how much it costs. Print out each item in the list with the same formatting, 
# using the .format method (not string concatenation). 
# For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00",
     "scarves, 13, 7.75"]
for inven in inventory :
    inven_split = inven.split(", ")
    print(type (inven_split))
    print(inven_split)
    print(inven_split[0])
    name_item= inven_split[0]
    how_many= inven_split[1]
    how_cost = inven_split[2]
    print (how_cost)
    print ("The store has {} {}, each for {} USD.".format(how_many,name_item,how_cost))