"""
Program: db_gui.py
Author: Cassandra Wruck
Date: 7/21/20

This program is to enter in information in gui that enters it in a table.
"""
import tkinter as tk
import sqlite3
from sqlite3 import Error
from tkinter import *

def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):

    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

#Query person table for person_id using first name and last name
def select_person_id(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()
    return rows # return the rows

conn = create_connection("pythonsqlite.db")


db = tk.Tk()


''' 
widgets are added here 
'''
db.title("Student and Person Table")

#Button "Create Database & Table"
#Copy the above code to set up database
#Table: person
#Table: student

create_table = tk.Button(db, text="Create table", width=25, command=create_tables).grid(row=1)

#Add row to person table

#call create_person function

#Read from GUI
#firstname
label_1 = tk.Label(db, text="First name: ")
label_1.grid(column=1,row=2)
first_name = tk.Entry(db, width=15).grid(column=2,row=2)

#lastname
label_2 = tk.Label(db, text="Last name: ")
label_2.grid(column=1,row=3)
last_name = tk.Entry(db, width=15).grid(column=2,row=3)

#create person tuple
person = (first_name, last_name)

#Button "Add Person"
add_person = tk.Button(db, text="Add Person", width=25).grid(row=4)
#command=create_person

#Create Student
#Read from GUI
#firstname student
label_3 = tk.Label(db, text="First name: ")
label_3.grid(column=1,row=5)
first_name_student = tk.Entry(db, width=15).grid(column=2,row=5)

#last name student
label_4 = tk.Label(db, text="Last name: ")
label_4.grid(column=1,row=6)
last_name_student = tk.Entry(db, width=15).grid(column=2,row=6)

#major
label_5 = tk.Label(db, text="Major: ")
label_5.grid(column=1,row=7)
major = tk.Entry(db, width=15).grid(column=2,row=7)

#startdate (text)
label_6 = tk.Label(db, text="Start Date: ")
label_6.grid(column=1,row=8)
start_date = tk.Entry(db, width=15).grid(column=2,row=8)

#create student tuple with major, startdate and person_id

student = (major,start_date, select_person_id(conn))

#Button "Add Student"
add_student = tk.Button(db, text="Add Student", width=25).grid(row=9)
#create student function

#Button: "View Person Table"
view_person = tk.Button(db, text="View Person", width=25).grid(row=10)
#Query for all rows of Person
#Display rows in the GUI

#Button: "View Student Table"
view_student = tk.Button(db, text="View Student", width=25).grid(row=11)
#Query for all rows of Person
#Display rows in the GUI

#Exit Button
exit_button = tk.Button(db, text='Exit', width=25, command=db.destroy)
exit_button.grid(row=12)


db.mainloop()
