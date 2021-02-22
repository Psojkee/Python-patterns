import json
import sqlite3

conn = sqlite3.connect('rosterdb1.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);


CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
)

''')

fname=input('vvedi')
if len(fname)<1:
    fname='roster_data.json'

data=open(fname).read()
json=json.loads(data)

for line in json:
    name=line[0]
    title=line[1]
    role=int(line[2])

    print(name,title)

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name,))
    cur.execute('SELECT id FROM USER WHERE name= ?', (name,))
    user_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title=?', (title,))
    course_id=cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, role))
    conn.commit()
