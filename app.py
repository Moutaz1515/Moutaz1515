from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=True)
	age = db.Column(db.Integer)

	def __repr__(self):
		return f"{self.name} - {self.age}"

@app.route('/')
def index():
	return 'this website developed by twitter: Almoutaz_Alz'

@app.route('/persons')
def get_persons():

	output = []
	person = Person.query.all()

	for per in person:
		data = {'name': per.name,'age': per.age}
		output.append(data)
	return {'person': output}
	
@app.route('/persons',methods=['POST'])
def add_person():
	person = Person(name = request.json['name'], age = request.json['age'])

	db.session.add(person)
	db.session.commit()

	return {'ID': person.id}
@app.route('/person/<id>',methods=['DELETE'])
def get_person(id):
	delete = Person.query.get(id)
	db.session.delete(delete)
	db.session.commit()
	return {"done": "the ID has been deleted"}

@app.route('/persons',methods=['DELETE'])
def delete_all():
	db.session.query(Person).delete()	
	db.session.commit()
	return {'has deleted': 'done'}






app.run(Debug=True)


			