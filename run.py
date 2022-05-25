from app import create_app, db
from app.models import CompanyModel

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/robinder/Documents/projects/japptracker/app.db"

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "CompanyModel": CompanyModel}