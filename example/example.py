from memrise import Course, Data


file = "test.db"
db = Data(file)

course = Course(2157577)
# Create file database output
db = Data(file)
# Connect to file database and init
db.init_database()
# Update information about the course
db.update_course(course)
# Update IPA for database
db.update_ipa()
# Translate the vocabulary to your own language
db.update_trans("vi")
# Close the database
db.close()
