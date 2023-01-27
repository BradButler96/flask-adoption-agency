from app import db
from models import Pet

db.drop_all()
db.create_all()

hendrix = Pet(name="Hendrix", 
              species="Pitbull", 
              photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbCDIdRmkk6-rRWZR6p5e6USUmk4U98M192w&usqp=CAU", 
              age=5,
              notes="He can be very annoying")

stella = Pet(name="Stella", 
             species="Maine Coon", 
             photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsmVmVqp89XGnfieZJIK1mcbC9f5zE6Z9k2w&usqp=CAU", 
             age=8,
             notes="She is the best pet",
             available=False)

gary = Pet(name="Gary", 
             species="Golden Retreiver", 
             photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrChh_XhVwZNixDdegJd-7aFYXSflE1JFSDQM8I3w79Y3YZGJUbb6hwmWF62m18xpJZc0&usqp=CAU", 
             age=3,
             notes="He likes to wear little booties",
             available=False)

db.session.add_all([hendrix, stella, gary])
db.session.commit()


