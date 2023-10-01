class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # законченные курсы
        self.courses_in_progress = []  # курсы в процессе
        self.grades = {}
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # закрепленные за преподователем курсы

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __str__(self):   # надо же попробовать
        return f'{self.name} {self.surname}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:  # если курс есть в (в ключе) оценках студента?
                student.grades[course] += [grade]  # то к нему добавляем оценку
            else:                        # ксли курса нет,
                student.grades[course] = [grade]   # то заводим его в ключ и первую оценку в значение
        else:
            return

one_lecturer = Lecturer('Алексей', 'Панин') # создаю лектора
one_lecturer.courses_attached += ['anatomy']  # закрепляю за лектором курс

best_student = Student('Иван', 'Алексеевич', 'пацан') # создаю студента
best_student.courses_in_progress += ['knitting'] # студент проходит следующие курсы
best_student.courses_in_progress += ['anatomy']
best_student.rate_hw(one_lecturer, 'anatomy', 2) # студент выставляет оценки лектору
best_student.rate_hw(one_lecturer, 'anatomy', 3)
best_student.rate_hw(one_lecturer, 'anatomy', 2)

cool_mentor = Mentor('Антонина', 'Эдуардовна')   # создаю студента
cool_mentor.courses_attached += ['knitting']   # закрепляю за ментором курс

print(f'Итого, у нас есть студент {best_student.name} {best_student.surname}, {best_student.gender} по жизни, который учится на курсах {", ".join(best_student.courses_in_progress)}')
print(f'Так же у нас есть лектор {one_lecturer}. Он преподает {", ".join(one_lecturer.courses_attached)}. Оценки лектора: {one_lecturer.grades}. ')
print(f'Ну и конечно ментор {cool_mentor.name} {cool_mentor.surname}. Она преподает {", ".join(cool_mentor.courses_attached)}')