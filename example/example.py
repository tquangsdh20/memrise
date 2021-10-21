from memrise import Course, Data
#Create file database output
db = Data('English.sqlite') #Other format is .db
#Connect to file database and init
db.init_database()

#Connect the course to scraping info this maybe take a few momment.
course = Course(1658724,2)
#Update information about the course
db.update_course(course)
