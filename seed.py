from app import db
from app.models import Company, Posting

db.drop_all()
db.create_all()
amzn = Company(name="AmAzON")
app1 = Posting(company=amzn)
app2 = Posting()
amzn.postings.append(app2)
db.session.add(amzn)
db.session.add(app1)
db.session.add(app2)
db.session.commit()
