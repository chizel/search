#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

def read_names():
    conn_string = "host='localhost' dbname='pdb' user='fordb' password='qwerty'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM names")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
#sort data from db
    res.sort()
    return res

def main():
    names = read_names()
    result = u''
    text = u'Илья Валентинович Сегалович — российский программист и общественный деятель, один из основателей (вместе со своим другом и одноклассником Аркадием Воложем) компании «Яндекс», ныне технический директор компании. Компания «Яндекс» — лидер на рынке поиска в России.'
    text = text.split()
    for word in text:
        print word
        if word not in names:
            result += word + ' '
        print result
        exit()
    print result

if __name__ == "__main__":
    main()
    read_names()
