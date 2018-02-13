# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:26:41 2017

@author: poaa
"""
import sqlite3
conn = sqlite3.connect(r'C:\Users\poaa\AppData\Local\Continuum\anaconda3\Library\bin\test.db')
c = conn.cursor()
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())
print()

#c.execute('Delete FROM stocks')
#conn.commit()


## Larger example that inserts many records at a time
#purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
#conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
print('')
t = ('IBM',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone()) #ojo pq si solo ejecutamos esto, solo saldría 1
print(c.fetchone())
print(c.fetchone())
conn.close()

