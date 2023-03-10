from peewee import *

user = 'root'
password = 'Mysql8'
host = 'localhost'
port = 3306
db_name = 'fastapi2'

database = MySQLDatabase(
    db_name, user=user,
    password=password,
    host=host,
    port=port
)


class User(Model):
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

