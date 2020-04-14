import sqlite3 
import os, sys

db_filepath=os.path.join(sys.path[0], "Movies.db")

def db_init():
    connection = sqlite3.connect(db_filepath) 

    # cursor  
    crsr = connection.cursor() 

    # creating the tables
    # reviews will store a dict(json object) that contains all the movies this person has reviewed
    # movies will store a dict that contains all the movies this person has reviewed.
    create_table="""CREATE TABLE IF NOT EXISTS users(
        user_name VARCHAR(20) PRIMARY KEY,
        reviews,
        movies,
        FOREIGN KEY(reviews) REFERENCES reviews(movie_name),
        FOREIGN KEY(movies) REFERENCES movies(movie_name)
    );"""
    crsr.execute(create_table)

    # comments will store a dict of all the users and their corresponding comments they posted. 
    # form will look like->
    # comments{ user: {date: 04-07-2018, text: this movie was trash. }}
    create_table="""CREATE TABLE IF NOT EXISTS reviews(
        movie_name VARCHAR PRIMARY KEY,
        review_text VARCHAR,
        comments VARCHAR,
        rating INTEGER,
        genre VARCHAR,
        year DATE,
        author VARCHAR,
        date_posted DATE,
        FOREIGN KEY(comments) REFERENCES comments(comment_text)
        );"""
    crsr.execute(create_table)

    create_table="""CREATE TABLE IF NOT EXISTS comments(
        author VARCHAR,
        movie VARCHAR PRIMARY KEY,
        comment_text VARCHAR,
        date_posted DATE,
        FOREIGN KEY(author) REFERENCES users(user_name)
        );"""
    crsr.execute(create_table)

    create_table="""CREATE TABLE IF NOT EXISTS movies(
        movie_name PRIMARY KEY,
        genre VARCHAR,
        year DATE,
        FOREIGN KEY(movie_name) REFERENCES users(movie_name)
    );"""
    crsr.execute(create_table)
    connection.commit()
    connection.close()
    return

# this will take a json object with a header specified as 'update' and parse it to determine which table
# needs to be updated with what value, or what value to remove.
# json is of form-> 
# {
# header:'update',
# new_value: 'value',
# is_delete: False
# location:
#   {
#       table_name:table,
#       entity:entity_name
#   }
# }

def db_update(obj):
    pass

# The search function will parse the incoming json blob to determine the location of the lookup info, then pass 
# it back to the server.py section and send it in a POST.
# json is of form-> 
# {
# header:'search',
# value: 'value',
# location:
#   {
#       table_name:table,
#       entity:entity_name
#   }
# }
# the function will pull the row and then parse that as a dict and return the relevant info.
def db_search(obj):
    pass

# This will take a json object with the header 'insert', locate the table and insert all values in their
# respective spots.
# json is of form-> 
# {
# header:'insert',
# table: table_name,
#  content':
#  {
#   'userName': 'here', 
#   'reviews': None,
#   'movies': None}
# }
def db_insert(obj):
    connection = sqlite3.connect(db_filepath) 

    # cursor  
    crsr = connection.cursor()
    if obj['table'] == 'users':

        tbl_insrt = [
            (
                obj['content']['userName'],
                obj['content']['reviews'],
                obj['content']['movies']
                
            ) 

        ]
        print(tbl_insrt)
        crsr.executemany("INSERT INTO users (user_name,reviews,movies) VALUES (?,?,?);", tbl_insrt)  
        crsr.execute("""SELECT * FROM users""")
        ans=crsr.fetchall()
        obj['header'] = 'emit'
        obj['content'] = [] #create a list to be filled with dictionaries that correspond to user entries in the table.
        #loop through the table and update the keys in the package to resend to the front end.
        for key in ans:
            obj['content'].append({'userName':key[0],'review':key[1],'movies':key[2]})
        print(obj)
        # we return the modified object to be sent to the frontend in response. Look at admin.vues axios post response.
        return obj 

    if obj['table'] == 'movies':
        pass

    if obj['table'] == 'reviews':
        pass

    if obj['table'] == 'comments':
        pass
    
    # connection.commit()
    connection.close()




















  ### Useful testing and pulling code ###

# # store all the fetched data in the ans variable 
# ans= crsr.fetchall()  
  
# # loop to print all the data 
# for i in ans: 
#     print(i) 

