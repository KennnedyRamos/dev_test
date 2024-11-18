from src.config.db import db

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    posts = db.relationship('Post', back_populates='user', lazy=True)

    def __repr__(self):
        return f"<User {self.firstName} {self.lastName}>"
