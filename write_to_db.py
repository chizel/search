#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import codecs

def read_names():
    f = codecs.open('first_names.txt', 'r', 'utf-8');
    data = f.read()
    names = data.split()
    return names


def main():
    conn_string = "host='localhost' dbname='pdb' user='fordb' password='qwerty'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    # execute our Query
    names = read_names()
    for name in names:
        cursor.execute("INSERT INTO names VALUES (\'%s\');" % name)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
