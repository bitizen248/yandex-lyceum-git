import sqlite3

a = input()
con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
            WHERE year >= 1997 and genre IN (
SELECT id FROM genres 
    WHERE title = 'музыка' or title = 'анимация')""").fetchall()

for elem in result:
    print(elem[0])

con.close()
print(123)
print(456)