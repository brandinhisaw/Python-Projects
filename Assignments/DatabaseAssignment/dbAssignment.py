import sqlite3

# establishes connection to the files.db
# creates the database if it does not already exist
conn = sqlite3.connect('files.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    # creates tbl_files if it doe not exist
    # establishes autoincrement primary key file_id and file_name column
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name STRING \
        )")
    # iterates through the fileList and checks extension
    # if the file ends in .txt, file name will be added to the table
    # the file name will also be printed to the console
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(file_name) VALUES(?)", \
                        (file,))
            print(file,)
    # commits executed SQL to the database
    conn.commit()
#closes the connection to the database
conn.close()

