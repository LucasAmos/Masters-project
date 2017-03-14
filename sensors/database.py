from sensors import app


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="lucasamos2",
    password="Fujifilm12",
    hostname="lucasamos2.mysql.pythonanywhere-services.com",
    databasename="lucasamos2$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

