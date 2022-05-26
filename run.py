import os
from app import create_app, db
from app.models import Posting, Company

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Company": Company, "Posting": Posting}