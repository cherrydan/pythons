#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Демонстрация функций модуля pymysql
"""
import sys

from  pymysql import *


def db_version(con):
    """
    Shows name and version
    of current MySQL DB

    con - DB connection
    """
    with con:
        cur = con.cursor()
        cur.execute('SELECT VERSION()')

        version = cur.fetchone()
        print('DB-version: {}'.format(version[0]))


def db_select(con, country):
    """
        Select some data from database

        con - DB-connection
        country  - string country name
    """ 

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM country_pop WHERE country=%s', country)
        rows = cur.fetchall()
        print('\nCountry\t\tYear\tPopulation')
        print()
        for row in rows:
            print("{0}\t{1}\t{2}".format(row[1], row[2], row[3]))

def main():
    con = connect('localhost', 'root', '',
                    'base')

    if len(sys.argv) < 2:
        country = input('Enter a country name ')
        db_select(con, country)
    elif sys.argv[1] == '--version':
        db_version(con)
    else:
        print('Unknown argument')
        sys.exit()

if __name__ == '__main__':
    main()
