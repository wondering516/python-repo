import sqlite3


import os
db_file ='site.db'

def create_table():


    if os.path.exit(db_file):

        conn = sqlite3.connect((db_file))

    cursor = conn.cursor()

    cursor.execute('''
        create table site(
            id integer primary key autoincrement,
            url :text
            
        
        )
    
    
    ''')

    conn.commit()

    conn.close()

def save(site):
    pass
