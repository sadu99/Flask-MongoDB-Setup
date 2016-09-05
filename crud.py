from flask import Flask 
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flask-mongo-db'
app.config['MONGO_URI'] = 'mongodb://sadu:sadu@ds019956.mlab.com:19956/flask-mongo-db'

mongo = PyMongo(app)

@app.route('/create')
def create():
	users_collection = mongo.db.users
	users_collection.insert({'name':'sadu', 'language':'Python'})
	users_collection.insert({'name':'kelly', 'language':'Java'})
	users_collection.insert({'name':'john', 'language':'C'})
	users_collection.insert({'name':'jack', 'language':'C++'})
	return "Added Users in DB!"

@app.route('/find')
def find():
	users_collection = mongo.db.users
	obj = users_collection.find_one({'name':'sadu'}) 
	return "%s Found! Favourite Language = %s" % (obj['name'], obj['language'])

@app.route('/update')
def update():
	users_collection = mongo.db.users
	obj = users_collection.find_one({'name':'sadu'}) 
	obj['language'] = "Java"
	users_collection.save(obj)
	return "Updated User!"

@app.route('/delete')
def delete():
	users_collection = mongo.db.users
	obj = users_collection.find_one({'name':'kelly'}) 
	users_collection.remove(obj)
	return "Deleted User!"	

if __name__=='__main__':
	app.run(debug=True)