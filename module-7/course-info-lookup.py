# Create a list of the courses, which will serve as our keys in the three dictionaries created
courses = ('CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241')

# Create three lists for the room, instructor, and meeting time, which will serve as our values in the dictionaries
rooms = ('3004', '4501', '6755', '1244', '1411')
instructors = ('Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee')
times = ('8:00 a.m.', '9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '1:00 p.m.')

# Zip together the key/value pairs and format as three new dictionaries
course_room_dict = dict(zip(courses, rooms))
course_instructor_dict = dict(zip(courses, instructors))
course_time_dict = dict(zip(courses, times))

# Gather course number from user input
print("Enter CSU Global course number: ")
course_num = input()

# Given the course number (key) print out the corresponding values in each of the three dictionaries
print(f"Room number: {course_room_dict[course_num]}")
print(f"Instructor: {course_instructor_dict[course_num]}")
print(f"Meeting time: {course_time_dict[course_num]}")