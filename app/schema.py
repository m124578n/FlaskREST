from .extensions import ma
from flask_marshmallow.fields import Hyperlinks, URLFor

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', '_links')

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user_detail", values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
