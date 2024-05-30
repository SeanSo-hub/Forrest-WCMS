from flask import request, jsonify
from config import app, db
from models import User


#users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_users})


@app.route("/create_user", methods=["POST"])
def create_user():
    fullname = request.json.get("fullname")
    contact_number = request.json.get("contactNumber")
    user_type = request.json.get("userType")

    if not fullname or not contact_number:
        return ( 
            jsonify({"message": "You must include a fullname and a contact number"}),
            400, 
        )
    
    new_user = User(
        fullname = fullname, 
        contact_number = contact_number, 
        user_type = user_type
    )
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created successfully!"}), 201


@app.route("/update_user/<int:user_id>")
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found!"}), 404
    
    data = request.json
    user.fullname = data.get("fullname", user.fullname)
    user.contact_number = data.get("contactNumber", user.contact_number)
    user.user_type = data.get("userType", user.user_type)

    db.session.commit()

    return jsonify({"message": "User updated successfully!"}, 200)


@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found!"}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"}, 200)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)    