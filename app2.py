from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

mysql_username = os.getenv("GCP_MYSQL_USERNAME")
mysql_password = os.getenv("GCP_MYSQL_PASSWORD")
mysql_host = os.getenv("GCP_MYSQL_HOSTNAME")

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + mysql_username + ':' + mysql_password + '@' + mysql_host + ':3306/patient_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #allows for tracking
app.secret_key = 'sdf#$#dfjkhdf0SDJH0df9fd98343fdfu34rf' #unique identifier 

db.init_app(app)

### Models ###
class Patients(db.Model):
    __tablename__ = 'production_patients'
    id = db.Column(db.Integer, primary_key=True)
    mrn = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    zip_code = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(255), nullable=True)

# this first function __init__ is to establish the class for python GUI
def __init__(self, mrn, first_name, last_name, zip_code, gender):
        self.mrn = mrn
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.gender = gender
        self.gender
# this second function is for the API endpoints to return JSON
    def to_json(self):
        return {
            'id': self.id,
            'mrn': self.mrn,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'zip_code': self.zip_code,
            'gender': self.gender
        }