#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import codecs

DB_NAME = 'pdb'
TABLE_NAME = 'useless_words'
FILE_NAME = 'useless_words.txt'

def read_words():
    try:
        f = codecs.open(FILE_NAME, 'r', 'utf-8')
        data = f.read()
        f.close()
    except IOError:
        print "Error! Can't open file!"

    words = data.split()

    for i in range(0, len(words)):
        words[i] = words[i].lower()

    #get unique values
    words = list(set(words))
    words.sort()
    return words


def main():
    conn_string = "host='localhost' dbname='" + DB_NAME + "' user='fordb' password='qwerty'"

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        words = read_words()

        for word in words:
            cursor.execute("""INSERT INTO %s VALUES ('%s');""" % (TABLE_NAME, word))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception , e:
        print 'ERROR:', e[0]
    return


if __name__ == "__main__":
    main()
