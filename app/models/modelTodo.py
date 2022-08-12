from utils.db import db

class Todo(db.Model):
    
    taskId = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))

    # con el created by puedo relacionar mas facil id y me ahorro claves foraneas
    created_by = db.Column(db.Integer())

    # ACA deberia isnertarle date time ds, al crear
    created_at = db.Column(db.String(30))
    #created_at = db.Column(db.current_timestamp())
    #created_at = db.Column('timestamp', db.TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    
    completed = db.Column(db.Boolean())
    
    def __init__(self, description,created_by, created_at, completed):
        self.description = description
        self.created_by = created_by
        self.created_at = created_at
        self.completed = completed


# __tablename__ = "tasks"

# # CREATE TABLE todo (
# #     id INT PRIMARY KEY AUTO_INCREMENT,
# #     created_by INT NOT NULL,
# #     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
# #     description TEXT NOT NULL,
# #     completed BOOLEAN NOT NULL,
# #     FOREIGN KEY (created_by) REFERENCES user (id)
# #     )