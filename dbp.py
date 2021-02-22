import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

link=input('put link here')
if (len(link)<1):
    link='mbox.txt'
fh=open(link)

for line in fh:
    if not line.startswith('From: '): continue
    pieces=line.split()
    email=pieces[1].split('@')
    org=email[1]
    cur.execute('SELECT count FROM Counts WHERE org= ? ', (org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        print(0)
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org =?', (org,))
        print(1)
    conn.commit()

checkdb = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(checkdb):
    print(str(row[0]),row[1])
cur.close()
