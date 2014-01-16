class Student:
      courseMarks={}
      name= ""
      def __init__(self, name, family):
      		self.name = name + " " + family
      		print("Student Created: " + self.name)
      def addCourseMark(self, course, mark):
           self.courseMarks[course] = mark
           print("Course Mark Added " + course + " " + str(mark))
      def average(self):
          count = 0
          avgSum = 0
          for grade in self.courseMarks.values():
            avgSum += grade
            count += 1
          print("Average: " + str(avgSum/count))

myStudent = Student("John", "Smith")
myStudent.addCourseMark("CMPUT 101", 80)
myStudent.addCourseMark("CMPUT 174", 85)
myStudent.addCourseMark("CMPUT 175", 90)
myStudent.average()
