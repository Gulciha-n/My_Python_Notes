class Lessons:
    def __init__(self,lesson_name,lesson_grade):
        self.lesson_name= lesson_name
        self.lesson_grade = lesson_grade

    def get_lesson_name(self):
        return f"Lesson name :{self.lesson_name}"
        
    def get_grade(self): 
        return f"Your grade is :{self.lesson_grade} :)"

lesson_name = input("Lesson name :")
lesson_grade = input("your grade :")
lesson1 = Lessons(lesson_name,lesson_grade)
print(lesson1.get_lesson_name())
print(lesson1.get_grade())


    