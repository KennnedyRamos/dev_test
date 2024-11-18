from src.config.db import db
from src.Entity.user import User

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    
    
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 

   
    user = db.relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post {self.title}>"
