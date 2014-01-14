#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2, codecs, sys, getopt

def read_words(file_name):
    try:
        f = codecs.open(file_name, 'r', 'utf-8')
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

def main(argv):
    DB_NAME = 'pdb'
    TABLE_NAME = 'useless_words'
    FILE_NAME = 'useless_words.txt'

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -f <inputfile> -t <table_name> -d <database_name>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -f <inputfile> -t <table_name> -d <database_name>'
            sys.exit()
        elif opt == "-f":
            FILE_NAME = arg
        elif opt == "-d":
            DB_NAME = arg
        elif opt == "-t":
            TABLE_NAME = arg

    conn_string = "host='localhost' dbname='" + DB_NAME + "' user='fordb' password='qwerty'"

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        words = read_words(FILE_NAME)

        for word in words:
            cursor.execute("""INSERT INTO %s VALUES ('%s');""" % (TABLE_NAME, word))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception , e:
        print 'ERROR:', e[0]

if __name__ == "__main__":
   main(sys.argv[1:])
