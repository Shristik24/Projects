""" Application:            English dictionary
    Author:                 Shristi Kumari
    Date of completion:     27-08-2020
    Database:               Global SQL server
##  Build a connection--point the cursor---run the query---fetch the data
    To improve:             Code is slow, multiple searches in same program instead of calling the \
                            script for each word,ouput display in a better user friendly format
"""


from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.filedialog import askopenfile
  
root = Tk() 
root.title("TitleName")
root.geometry('200x200') 



import mysql.connector
from difflib import get_close_matches




db_cursor=''
query_result=''
def sql_connection():
    con=mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    return con

def user_input(sys_in='None'):
    if sys_in=='None':
        user_in=str(HeaderName.get())
        search_word=[user_in.lower(),user_in.title(),user_in.upper()]
    else:
        search_word=[sys_in.lower(),sys_in.title(),sys_in.upper()]
    return search_word
    
def db_query(search_word):
        db_cursor=conn.cursor()
        db_cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression= '{search_word[0]}' OR Expression= '{search_word[1]}' OR Expression= '{search_word[2]}'")
        result=db_cursor.fetchall()
        if result:
            for item in result:
                mb.showinfo('Meaning',item[0])
        else:
            db_cursor.execute("SELECT Expression FROM Dictionary ")
            expr=db_cursor.fetchall()
            #close_match(expr,search_word)

            
def close_match(expr,search_word):
        new_expr=[]
        for item in expr:
            new_expr.append(item[0])
        close_word=get_close_matches(search_word[0],new_expr,cutoff=0.8)
        if len(close_word)>0:
            yn=input(f"Did you mean {close_word[0]}? Enter Y for yes and N for No : ")
            if yn=="Y":
                word_research=user_input(sys_in=close_word[0])
                db_query(word_research)
            else:
                print("Check the word and try again")
        else:
            print("Word not found")

def browse_button():
	global filename
	word=user_input()
	db_query(word)			


conn=sql_connection()


TypeBrowse = Button(root, text ='Open', command = browse_button) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)

HeaderName = Entry(root, width=10)
HeaderName.pack()
HeaderName.place(x=0,y=0)



mainloop()
