import os
from app import create_app, db
from app.models.company import Company
from app.models.posting import Posting
from app.models.user import User
from app.models.interview import Interview
from app.models.file import File

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Company": Company, "Posting": Posting,
            "User": User, "Interview": Interview, "File": File}