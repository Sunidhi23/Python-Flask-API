from flask import Flask,render_template,request, jsonify
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "sunidhi"
app.config['MYSQL_DB'] = "audiolibrary"

mysql = MySQL(app) 
givenUsername = 'root'


@app.route("/<string:filetype>/<int:fileid>",methods=['GET'])   #READ API
def indexget(filetype,fileid):
	try:
		cur = mysql.connection.cursor()
		query = "SELECT * FROM {} WHERE ID ='{}'".format(filetype ,fileid)
		print(query)
		cur.execute(query) #,userAuthInfo
		result = cur.fetchall()
		print(result)
		cur.close()
		return jsonify(result), 200
	except:
		return jsonify('500 Internal Server Error')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'400': 'bad request'}), 400)

@app.route("/<string:filetype>/<int:fileid>",methods=['DELETE'])   # FOR DELETE API
def indexdelete(filetype,fileid):
	try:
		cur = mysql.connection.cursor()
		query = "DELETE FROM {} WHERE ID ='{}'".format(filetype ,fileid)
		print(query)
		cur.execute(query) 
		mysql.connection.commit()
		cur.close()
		return jsonify(200, 'OK'), 200
	except:
		return jsonify('500 Internal Server Error')


@app.route("/<string:filetype>/<int:fileid>",methods=['PUT', 'POST'])   #FOR UPDATE API
def indexupdate(filetype,fileid):
	print(request.json)
	#return jsonify('ok'), 200
	if filetype == 'song':
		songname = request.json.get('songname')
		songduration = request.json.get('songduration')
		songuploadtime = request.json.get('songuploadtime')
	
	if filetype == 'podcast':
		podcastname = request.json.get('podcastname')
		podcastduration = request.json.get('podcastduration')
		podcastuploadtime = request.json.get('podcastuploadtime')
		Host = request.json.get('Host')
		Participants = request.json.get('Participants')

	if filetype == 'audiobook':
		audiobooktitle = request.json.get('audiobooktitle')
		author = request.json.get('author')
		narrator = request.json.get('narrator')
		audiobookduration = request.json.get('audiobookduration')
		audiobookuploadtime = request.json.get('audiobookuploadtime')
	
	cur = mysql.connection.cursor()

	if request.method == 'POST':
		
		if filetype == 'song':
			cur.execute("INSERT INTO song (ID,songname,songduration,songuploadtime) VALUES (%s, %s, %s, %s)", (fileid,songname,songduration,songuploadtime))
		if filetype == 'podcast':
			cur.execute("INSERT INTO podcast (ID,podcastduration,podcastname,podcastuploadtime, Host, Participants) VALUES (%s, %s, %s, %s, %s, %s)", (fileid,podcastduration,podcastname,podcastuploadtime, Host, Participants))
		if filetype == 'audiobook':
			cur.execute("INSERT INTO audiobook (ID,audiobooktitle,author,narrator, audiobookduration, audiobookuploadtime) VALUES (%s, %s, %s, %s, %s, %s)", (fileid,audiobooktitle,author,narrator, audiobookduration, audiobookuploadtime))

	if request.method == 'PUT':

		if filetype == 'song':
			cur.execute('UPDATE song SET songname = %s, songduration = %s, songuploadtime = %s WHERE ID = %s', (songname,songduration,songuploadtime, fileid))
		if filetype == 'podcast':
			cur.execute("UPDATE podcast SET podcastduration = %s, podcastname = %s, podcastuploadtime = %s, Host = %s, Participants = %s WHERE ID = %s", (podcastduration,podcastname,podcastuploadtime, Host, Participants, fileid))
		if filetype == 'audiobook':
			cur.execute("UPDATE audiobook SET audiobooktitle = %s,author = %s, narrator = %s, audiobookduration = %s, audiobookuploadtime = %s WHERE ID = %s", (audiobooktitle,author,narrator, audiobookduration, audiobookuploadtime, fileid))

	mysql.connection.commit()
	cur.close()
	return jsonify(200, 'OK'), 200



@app.route("/<string:filetype>/",methods=['POST'])   #For CREATE API
def indexcreate(filetype):
	
	fileid = 1

	if filetype == 'song':
		songname = request.json.get('songname')
		songduration = request.json.get('songduration')
		songuploadtime = request.json.get('songuploadtime')
	
	if filetype == 'podcast':
		podcastname = request.json.get('podcastname')
		podcastduration = request.json.get('podcastduration')
		podcastuploadtime = request.json.get('podcastuploadtime')
		Host = request.json.get('Host')
		Participants = request.json.get('Participants')

	if filetype == 'audiobook':
		audiobooktitle = request.json.get('audiobooktitle')
		author = request.json.get('author')
		narrator = request.json.get('narrator')
		audiobookduration = request.json.get('audiobookduration')
		audiobookuploadtime = request.json.get('audiobookuploadtime')
	cur = mysql.connection.cursor()

	if request.method == 'POST':
		
		if filetype == 'song':
			cur.execute("CREATE TABLE song (ID INT NOT NULL PRIMARY KEY,songname VARCHAR(100) NOT NULL,songduration INT unsigned NOT NULL,songuploadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL)")
			cur.execute("INSERT INTO song (ID,songname,songduration,songuploadtime) VALUES (%s, %s, %s, %s)", (fileid,songname,songduration,songuploadtime))
		if filetype == 'podcast':
			cur.execute("CREATE TABLE podcast (ID INT NOT NULL PRIMARY KEY,podcastname VARCHAR(100) NOT NULL,podcastduration INT unsigned NOT NULL,podcastuploadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL, Host VARCHAR(100) NOT NULL, Participants VARCHAR(100) )")
			cur.execute("INSERT INTO podcast (ID,podcastduration,podcastname,podcastuploadtime, Host, Participants) VALUES (%s, %s, %s, %s, %s, %s)", (fileid,podcastduration,podcastname,podcastuploadtime, Host, Participants))
		if filetype == 'audiobook':
			cur.execute("CREATE TABLE audiobook (ID INT NOT NULL PRIMARY KEY,audiobooktitle VARCHAR(100) NOT NULL,author VARCHAR(100) NOT NULL, narrator VARCHAR(100) NOT NULL, audiobookduration INT unsigned NOT NULL, audiobookuploadtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL)")
			cur.execute("INSERT INTO audiobook (ID,audiobooktitle,author,narrator, audiobookduration, audiobookuploadtime) VALUES (%s, %s, %s, %s, %s, %s)", (fileid,audiobooktitle,author,narrator, audiobookduration, audiobookuploadtime))
	mysql.connection.commit()
	cur.close()
	return jsonify(200, 'OK'), 200


if __name__ == '__main__':
	app.run(debug=True)