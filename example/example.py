from memrise import Course,Database

db = Database('English.sqlite')
db.connect()
db.init()
course = Course(1658724,2)
course.update(db)
levels = course.get_levels()
for level in levels:
    level.update(db)

db.update_db_en(1658724,'fr')
