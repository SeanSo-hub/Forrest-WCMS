from config import db
from enum import Enum

class UserType(Enum):
    STUDENT = "student"
    EMPLOYEE = "employee"
    OTHERS = "others"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), unique=False, nullable=False)
    contact_number = db.Column(db.String(11), unique=False, nullable=False)
    # user_type = db.Column(db.Enum(UserType), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "fullName": self.fullname,
            "contactNumber": self.contact_number,
            # "userType": self.user_type.value,
        }
    
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }
