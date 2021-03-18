from . import db
from  werkzeug.security import generate_password_hash


class PropertyTable(db.Model):
    __tablename__ = 'properties_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    option = db.Column(db.String(80))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(80))

    def __init__(self, title, bedrooms, bathrooms, location, price, option, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.option = option
        self.description = description
        self.photo = photo

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2 support
    #     except NameError:
    #         return str(self.id)  # python 3 support

    # def __repr__(self):
    #     return '<User %r>' % (self.username)
