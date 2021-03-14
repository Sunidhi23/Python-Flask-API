import mysql.connector

def insert_into_songtable(songID, songname, songduration, songuploadtime):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='audiolibrary',
                                             user='root',
                                             password='sunidhi')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO song (ID, songname, songduration, songuploadtime) 
                                VALUES (%s, %s, %s, %s) """

        song_metadata = (songID, songname, songduration, songuploadtime)
        cursor.execute(mySql_insert_query, song_metadata)
        connection.commit()
        print("Song_Track inserted successfully into Song table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert_into_audiobooktable(audiobookID, audiobooktitle, author, narrator, audiobookduration,audiobookuploadtime):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='audiolibrary',
                                             user='root',
                                             password='sunidhi')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO audiobook (ID, audiobooktitle, author, narrator, audiobookduration,audiobookuploadtime) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

        audiobook_metadata = (audiobookID, audiobooktitle, author, narrator, audiobookduration,audiobookuploadtime)
        cursor.execute(mySql_insert_query, audiobook_metadata)
        connection.commit()
        print("Audio_Track inserted successfully into audiobook table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")    

def insert_into_podcasttable(podcastID, podcastname, podcastduration, podcastuploadtime, Host,Participants):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='audiolibrary',
                                             user='root',
                                             password='sunidhi')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO podcast (ID, podcastname, podcastduration, podcastuploadtime, Host,Participants) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

        podcast_metadata = (podcastID, podcastname, podcastduration, podcastuploadtime, Host,Participants)
        cursor.execute(mySql_insert_query, podcast_metadata)
        connection.commit()
        print("Pocast_track inserted successfully into audiobook table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")    

if __name__ == '__main__':
	insert_into_songtable(1,"loco_poco",150,'2021-03-12 14:30:21')
	insert_into_songtable(2,"calma",189,'2021-03-12 17:10:22')
	insert_into_audiobooktable(1, "wingsoffire", "Abdul Kalam", "Suresh saha", 1000,'2021-03-12 17:30:21')
	insert_into_audiobooktable(2, "awaken the giant within", "Athony robbins", "Melona rusk", 1876,'2021-03-12 18:30:22')
	insert_into_podcasttable(1,"willywin","1200",'2021-03-12 19:30:21',"winson","Tina")
	insert_into_podcasttable(2,"autum here","1800",'2021-03-12 10:30:21',"Kishor","Hari")






