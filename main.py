class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # законченные курсы
        self.courses_in_progress = [] # курсы в процессе
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        result = 0.0
        list_ratings = []
        for value in self.grades.values():
          list_ratings.extend(value)
          if len(list_ratings) == 0:
              result = 0
          else:
              result = sum(list_ratings) / len(list_ratings)
        return result

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, student):
        return self.average() < student.average()

    def __gt__(self, student):
        return self.average() > student.average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # закрепленные за преподователем курсы
    def __str__(self):  # надо же попробовать
        return f'{self.name} {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def average(self):
        list_ratings = []
        result = 0.0
        for value in self.grades.values():
          list_ratings.extend(value)
          if len(list_ratings) == 0:
              result = 0
          else:
              result = sum(list_ratings) / len(list_ratings)
        return f'{result }'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {one_lecturer.average()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

one_lecturer = Lecturer('Алексей', 'Панин')     # создаю лектора
two_lecturer = Lecturer('Вася', 'Степочкин')    # второй лектор
one_lecturer.courses_attached += ['anatomy']    # закрепляю за лектором курсы
one_lecturer.courses_attached += ['biology']
two_lecturer.courses_attached += ['biology']

best_student = Student('Иван', 'Царевич', 'пацан')       # создаю студента
woman_student = Student('Василиса', 'Премудрая', 'дева') # второй студент
best_student.courses_in_progress += ['anatomy']          # студенты проходят следующие курсы
best_student.courses_in_progress += ['biology']
best_student.courses_in_progress += ['parallel_drawing']
woman_student.courses_in_progress += ['anatomy']
woman_student.courses_in_progress += ['parallel_drawing']  # ////
best_student.finished_courses += ['python']
best_student.rate_hw(one_lecturer, 'anatomy', 2)         # студенты выставляют оценки лектору
best_student.rate_hw(one_lecturer, 'anatomy', 2)
best_student.rate_hw(one_lecturer, 'biology', 3)
best_student.rate_hw(one_lecturer, 'biology', 4)
woman_student.rate_hw(one_lecturer, 'anatomy', 2)

cool_mentor = Mentor('Антонина', 'Эдуардовна')  # создаю ментора
super_cool_mentor = Mentor('Альберт', 'Энштейн')      # второй ментор
cool_mentor.courses_attached += ['knitting']    # закрепляю за ментором курс

some_reviewer = Reviewer('Аграфена', 'Рудольфовна')     # создаю Reviewer
which_reviewer = Reviewer('Джек', 'Воробей')            # второй Reviewer
some_reviewer.courses_attached += ['parallel_drawing']  # закрепляю за ревьювером курс
some_reviewer.rate_hw(best_student, 'parallel_drawing', 4)
some_reviewer.rate_hw(best_student, 'parallel_drawing', 5)
some_reviewer.rate_hw(woman_student, 'parallel_drawing', 5)
some_reviewer.rate_hw(best_student, 'anatomy', 4)
some_reviewer.rate_hw(woman_student, 'anatomy', 5)
print()
print(best_student > woman_student)
print(best_student < woman_student)
print()
# print(f'Итого, у нас есть студент {best_student.name} {best_student.surname}, {best_student.gender} по жизни, который учится на курсах {", ".join(best_student.courses_in_progress)}.')
# print(f'Так же у нас есть лектор {one_lecturer.name} {one_lecturer.surname}. Он преподает {", ".join(one_lecturer.courses_attached)}. Оценки лектора: {one_lecturer.grades}. ')
# print(f'Ну и конечно ментор {cool_mentor.name} {cool_mentor.surname}. Она преподает {", ".join(cool_mentor.courses_attached)}.')
print(some_reviewer)
print()
print(one_lecturer)
print()
print(best_student)

students_list = [best_student, woman_student]

def average_course(students_, course):
    list_ratings = []  # список оценок
    for student in students_:  # студент
        for key, value in student.grades.items():  # курс, оценки
            # print(key)
            # print(value)
            if key == course:
                list_ratings += value
    return round(sum(list_ratings) / len(list_ratings), 2)
print()
print(f"Средний бал по курсу {'parallel_drawing'}:")
print(average_course(students_list, 'parallel_drawing'))