import sqlite3

database = '' # path to the sqllite database found in Google/Chrome/User Data/Default/History
conn = sqlite3.connect(database)
c = conn.cursor()

print('Hi!, type :')
print('1. clear => clears all history') 
print('2. show  => shows all history')
print('3. if you want to clear a specific url enter its name i.e youtube', '\n')


arg = str(input('enter a keyword: '))
ids = []

if arg == 'clear':
    c.execute('DELETE FROM urls')
    print(f'We have deleted {c.rowcount} records from the table ...')
    conn.commit()
    conn.close()
        
elif arg == 'show':
    for rows in c.execute("SELECT id, url FROM urls"):
        print(rows[1])
        ids.append(rows[0])

    print(f'{len(ids)} records found ...')

else:
    result = True

    while result:
        result = False
        id = 0
        for rows in c.execute(f"SELECT id, url FROM urls WHERE url LIKE '%{arg}%'"):
            id = rows[0]
            ids.append((id,))
            
        print(f'{len(ids)} records found ...')

        c.executemany('DELETE FROM urls where id=?', ids)
        conn.commit()
        conn.close()