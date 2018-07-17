'''
Created on 11 мая 2018 г.

@author: danny

Displays with prettyTable library
'''

#-*- coding:utf-8-*-

from prettytable import PrettyTable

table = PrettyTable(["Product", "Qty"])



picnicItems = {'sandwiches': 4, 'apples':12, 'cups': 4, 'wine':2,
               'cookies': 8000}



for k,v in picnicItems.items():
    table.add_row([k,str(v)])



'''
table.add_row(["sandwiches", 4])
table.add_row(["apples", 12])
table.add_row(["cups", 4])
table.add_row(["cookies",900])
'''

table.sort_key("Qty")



print(table)