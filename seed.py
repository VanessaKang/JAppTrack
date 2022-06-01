from app import db
from datetime import datetime, timedelta

from app.models.application import Application
from app.models.company import Company
from app.models.interview import Interview
from app.models.posting import Posting
from app.models.user import User
from app.models.file import File, FileTypeEnum

db.drop_all()
db.create_all()

location = "Los Angeles"
position_title = "Software Development Engineer"
url = "https://www.amazon.jobs/en/jobs/994952/senior-software-development-engineer"
source = "glassdoor"
first = "Vanessa"
last = "Kang"
username = "vkang"
email = "email@gmail.com"



amazon = Company(name="Amazon")
meta = Company(name="Meta")
sde_posting = Posting(position_title=position_title, location=location, url=url, company=amazon, source=source)
test_posting =Posting(position_title='Test Engineer', location=location, url=url, company=meta, source=source)


user1 = User(first_name=first, last_name=last, username=username, password_hash='1234', email=email)
# user2 = User(first_name="robin", last_name="goyal", username="rgoyal", password_hash="ilv",email="bob@Bob.com")

ResumeFile = File(type='resume', name='VanessaResume')
CLFile = File(type='resume', name='VanessaCoverLetter')


amazon_app = Application(posting=sde_posting, user=user1)
meta_app = Application(posting=test_posting, user=user1)
db.session.add(amazon)
db.session.add(meta)
db.session.commit()

interview1 = Interview(scheduled_date=datetime.utcnow(), application=amazon_app, type='coding')
interview2 = Interview(scheduled_date=datetime.utcnow()+timedelta(days=5), application=amazon_app, type='system_design')
interview3 = Interview(scheduled_date=datetime.utcnow()+timedelta(days=10), application=meta_app, type='system_design')

db.session.add(amazon)
db.session.add(meta)
db.session.add(sde_posting)
db.session.add(test_posting)
db.session.add(amazon_app)
db.session.add(meta_app)
db.session.add(interview1)
db.session.add(interview2)
db.session.add(interview3)
db.session.add(user1)
# db.session.add(user2)

db.session.commit()
