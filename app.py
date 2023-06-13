from app import create_app
from app.model import User
from app.schema import user_schema, users_schema

from flask_restful import Resource, Api

app = create_app()

# api = Api(app)

# class UserPage(Resource):
#     def get(self):
#         all_users = User.query.all()
#         return users_schema.dump(all_users)
    
# api.add_resource(UserPage, '/')


@app.route("/api/users/")
def users():
    all_users = User.query.all()
    print(all_users)
    return users_schema.dump(all_users)


@app.route("/api/users/<id>")
def user_detail(id):
    user = User.query.get(id)
    return user_schema.dump(user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
