# I tried to do this assignment but I simply couldn't get Sequel to work...





# Place any necessary imports here
import sqlite3
import json

####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
import parsers.py

####################################################
# Part 1
####################################################

def populateDatabase(databaseName, wordCounts, metaData):
     conn = sqlite.connect(databaseName)
    c = conn.cursor()
    c.execute(‘’’CREATE TABLE speechWordCounts (filename text, word_speech text, count integer)’’’)
    c.execute(‘’’CREATE TABLE metaData (number integer, start date, end date, president text, prior text, party text, vice text)’’’)
    for key,value in wordCounts.items():
        for a,b in value.items():
            c.execute('''INSERT INTO speechWordCounts (filename,word_speech,count) values (key,a,b)''')

    conn.commit() # save (commit) the changes
    conn.close()

    
    #I simply couldn't get this to run, I tried working on it for a long time trying various things,
    #but my query statements wouldn't work.
    
    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    return 0

# Test your code here

####################################################
# Part 2
####################################################


#### I tried doing this part, but I have no idea if it works because my part 1 code didn't
#### run so I couldn't test it. I understand the concept of selecting from columns, and
#### searching for things, but I don't know.

def searchDatabase(databaseName, word): 
    conn = sqlite.connect(databaseName)
    c=conn.cursor()
    c.execute('''SELECT MAX(count) AS t FROM speechWordCounts WHERE word_speech == word''')    
    c.execute('''SELECT filename AS ret FROM speechWordCounts WHERE count == t AND WHERE word_speech == word''')
    print(ret)
    conn.commit()
    conn.close()
        
    
    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    #          the highest count of the target word
    return 0

def computeLengthByParty(databaseName, word): 
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    return 0
        
