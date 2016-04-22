import rom

# All models to be handled by rom must derived from rom.Model
class User(rom.Model):
    email = rom.String(required=True, unique=True, suffix=True)
    salt = rom.String()
    password = rom.String()
    created_at = rom.Float(default=time.time)

class Post(rom.Model):
    user = rom.String(required=True)
    title = rom.String(required=True)
    text = rom.String(required=True)
    created_at = rom.Float(default=time.time)