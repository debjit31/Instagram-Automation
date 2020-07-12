from instabot import Bot
from secrets import username, password
import time
from datetime import datetime
b = Bot()

b.login(username= username, password = password)

## add files to directory and add their names to the files list
## after they are uploaded all files will be automatically deleted
files = ["file"]
for i in files:
	fname  = i+".jpg"
	b.upload_photo(fname, caption = "Uploaded by instabot #PythonAutomation AUTOMATING INSTAGRAM")
	time.sleep(5)
