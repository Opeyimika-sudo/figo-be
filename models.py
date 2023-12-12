from app import db
from datetime import datetime

class Images(db.Model):
    __tablename__ = 'images'

    user_id = db.Column(db.Integer(), primary_key=True)
    image_url = db.Column(db.String(), nullable=False, unique=True)
    image_desc = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)

    def __init__(self, image_url, image_desc):
        self.image_url = image_url
        self.image_desc = image_desc

    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def to_dict(self):
      return {
          'id': self.user_id,
          'image_url': self.image_url,
          'image_desc': self.image_desc,
          'created_on': self.created_on
      }