import os , sqlite3




def validate(file_name):
    return file_name in os.listdir(os.getcwd())


def create_table():
    file_name=raw_input('Enter table name: ') + '.db'
    if validate(file_name):
        ans=raw_input('Such file exist, do you want to overwrite? Y or N \n')
        if ans in 'nN':
            print_dir()
            return
    else:
        conn= sqlite3.connect(file_name)
    conn.execute(''' CREATE TABLE USERS (
    ID INT PRIMARY KEY,
    NAME TEXT,
    RATING INT )''')

    conn.close()

def delete_table():
    file_name=raw_input('What table do you want to delete? ') + '.db'
    if validate(file_name):
        os.remove(file_name)
        print 'Deleted'
    else:
        print 'Not such table'

actions={'c':create_table, 'd': delete_table} # 'i':insert_intable}

while True:
    ans=raw_input('What to do?\n' +
                  " 'n' to exit"+
                   " 'c' to create table " +
                    "'d' to delete table " )
    if ans in 'nN':
        break
    elif ans in actions:
        actions[ans]()
    else:
        print 'Unknown symbol'
print 'Exited'
