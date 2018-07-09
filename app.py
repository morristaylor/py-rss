from flask import Flask

app = Flask(__name__)
db_uri = 'mysql+pymysql://root:homespringmaria@localhost/feedreader'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# and no that's not my ~actual~ root password... it's just one for this project :)
