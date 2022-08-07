from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    db = "alex"
    def __init__(self,data):
        self.id = data['id']
        self.contact = data['contact']
        self.message = data['message']

    @classmethod
    def save(cls,data):
        query ="INSERT INTO messages (contact, message) VALUES (%(contact)s,%(message)s);"
        return connectToMySQL(cls.db).query_db(query,data)