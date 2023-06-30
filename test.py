import random


# function to make a list of random 10 number from 0 to 9
def make_list():
    list = []
    for i in range(10):
        list.append(random.randint(0, 9))
    return list

#find the most common number in a list of lists
def many_lists():
    list_list = []
    
    for i in range(10):
        list_list.append(make_list())


# a function to show the number of appearances of each number from 0 to 9

def show_list(list):
    for i in range(10):
        