from utils.db import db

class Todo(db.Model):
    
    taskId = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    created_by = db.Column(db.Integer())
    created_at = db.Column(db.String(30))
    completed = db.Column(db.Boolean())
    
    def __init__(self, description,created_by, created_at, completed):
        self.description = description
        self.created_by = created_by
        self.created_at = created_at
        self.completed = completed
