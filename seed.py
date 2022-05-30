from app import db
from datetime import datetime, timedelta

from app.models.application import Application
from app.models.company import Company
from app.models.interview import Interview
from app.models.posting import Posting
from app.models.user import User

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
sde_posting = Posting(position_title=position_title, location=location, url=url, company=amazon, source=source)

user1 = User(first_name=first, last_name=last, username=username, email=email)
user2 = User(first_name="robin", last_name="goyal", username="rgoyal", email="bob@Bob.com")

amazon_application1 = Application(posting=sde_posting, user=user1)
amazon_application2 = Application(posting=sde_posting, user=user2)

interview1 = Interview(application=amazon_application1, date=datetime.utcnow(), type='coding')
interview2 = Interview(application=amazon_application1, date=datetime.utcnow()+timedelta(days=5), type='system_design')

db.session.add(amazon)
db.session.add(sde_posting)
db.session.add(amazon_application1)
db.session.add(amazon_application2)
db.session.add(interview1)
db.session.add(interview2)

db.session.commit()
