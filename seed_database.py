import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model

from server import app

os.system("dropdb car_meet")
os.system("createdb car_meet")

model.connect_to_db(app)
app.app_context().push()
model.db.create_all()
