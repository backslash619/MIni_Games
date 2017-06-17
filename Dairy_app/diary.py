#!/usr/bin/env python3


# we are creating a model for our diary application after that change the mode of .py file using chmod +x ___.py
# adding the shabang line which tells the system to run in which format
from collections import OrderedDict
import os
import datetime
import sys
# collections holds large number of great built in functuon /methods like named_tuple
# above are python imports and below are the third party imports
from peewee import *

# record our thoughts and stuff remembring things and on that we put together timestamp on it and save
# it in adatabase
db = SqliteDatabase('diary_database.db')
flag = False


# using  for best practice  ie. making a base model and using a variable which pints out to the database object and then
# our rest models can extend it this Model class is from peewee

class Basemodel(Model):
    class Meta:
        database = db


class Entry(Basemodel):
    # content
    # textfield is used against VARCHAR there is limited space to hold the content
    # but in textfield you can hold as much as you can
    content = TextField()  # textfield is from peewee built-in

    # timestamp
    # in timestamp we use our built-in peewee Datefield()
    timestamp = DateTimeField(default=datetime.datetime.now)  # didn't use the parenthesis
    # becoz of that it gives the time of the script started time not now time hence we dropeed the parenthesis


# initialize the database or say create database
def initialize():
    """create the database and table if they don't exists"""
    db.connect()
    db.create_tables([Entry], safe=True)


def clear_screen():
    """clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


# creating a menu loop to CRUD something from the database on chossing what to do

def menu_loop():
    """Shows the menu"""
    choice = None  # setting up a variable to none

    while choice != 'q':  #
        clear_screen()

        print("Enter q to quit.")
        print("-+-+" * 5 + "MENU" + "-+-+" * 5)
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))  # printing key and value as our
            # print("-+-+" * 15)
            # key --> values in the ordered dict are the functions also so they are functions
            # and __doc__ is the docstring of that function this prints out {key}) and then {doct string inside the function}#
        print("-+-+" * 11)
        choice = input("Action:").lower().strip()  # ask what is their choice as from
        #  printing the the menu and we lower case it and strip it off


        if choice in menu:
            clear_screen()
            #  only if it's in the menu then ..
            menu[choice]()
            # we check if its q  then quit if not then we come back to our menu and run that function as menu[choice]()
            # here choice as a, v for add entry or view entry if does'nt go into the while loop then exits


def add_entry():
    """adds a an entry """
    print("Enter your entry. press ctrl+d when finished.")
    data = sys.stdin.read().strip()
    # we are using the sys module of pyton which gives us the control over everything what
    # the user type from the keyboard we read it and strip off any spaces or anything else
    if data:  # make sure we got something
        if input("Do you want to save this? [Y/n] ").lower() != 'n':
            Entry.create(content=data)
            print("Saved Successfully!!")
        else:
            print("Entry is being discarded!!")


def view_entries(search_query=None, ):
    """view previous entries """
    # getting all the entries
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        # here we are only filtering the data it's not a sub query just a filtering clause is where the content contains the search_query text we have input
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:

        timestamp = entry.timestamp.strftime(
            '%A %B %d, %Y %I:%M%p')  # here we are making the timestamp into string and
        #  %A weekday   # %B month name   # %d number   # %Y year   # %I hour 12 hour clock   # %M minute   # %p am/pm printing out hte tumestamp
        clear_screen()
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print("\n\n" + '=' * len(timestamp))
        print('n} next entry')
        print('d) delete entry')
        print('q} return to main menu')

        next_action = input("Action:[Ndq]  ").lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
    # if we press anything then q go to the next entry
    print("Database is empty now, no more entries!!")

def search_entries():
    """search entries for a string """
    search_query = input('Search query: ')
    view_entries(search_query, )


def delete_entry(entry):
    """delete an entry """
    # deleting the entry while reading one as entry as
    # arguement comes here is the actual model instance of our database
    # contains all the attributes content timestamp
    if input('Are you sure? [y/N]').lower() == 'y':
        entry.delete_instance()

        # here the model instace take the current instace
        # which points to hte row of the database
        # here it is used in view method as we delte the entry  we get to see the
        # next one its cool that all this work together #


#######################----------menu----------##################
# In ordered dict we use list to store the data using further tuples as data items
# each of our items are tuple best way to create dict
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])
# keys goes in as come out lifo is applies as last = true for fifo we use last = false
####################################################################

if __name__ == '__main__':
    initialize()  # we run before the menu loop becoz we want the updated table data to show up
    menu_loop()
