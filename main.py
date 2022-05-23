class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # метод добавления завершенных курсов (из первоначального условия квиза)
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # метод добавления нового курса для изучения
    def add_new_course(self, course):
        self.courses_in_progress.append(course)

    # метод удаления курса из текущих
    def delete_course_in_progress(self, course_name):
        self.courses_in_progress.remove(course_name)

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lector_grades:
                lector.lector_grades[course] += [grade]
            else:
                lector.lector_grades[course] = [grade]
        else:
            return 'Ошибка'

    # метод принтования
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.all_grades_student()} \nКурсы в процессе изучения: {self.course_in_progress_str()} \nЗавершенные курсы: {self.finished_courses_str()} '
        return res

    # рассчет средней оценки студента по всем курсам (вспомагательный для метода __str__)
    def all_grades_student(self):
        list_self_grades = []

        for course in self.grades:
            list_self_grades.extend(self.grades[course])

        # for course in other.grades:
        #   list_other_grades.extend(other_grades[course])

        if len(list_self_grades) > 0:
            grades_of_sudent = round(sum(list_self_grades) / len(list_self_grades), 1)
            return grades_of_sudent
        else:
            return 'У студента нет оценок'

    # курсы в процессе изучения (вспомагательный для метода __str__)
    def course_in_progress_str(self):
        course_in_progress_str = ",".join(self.courses_in_progress)
        return course_in_progress_str

    # завершенные курсы(вспомагательный для метода __str__)
    def finished_courses_str(self):
        finished_courses_str = ",".join(self.finished_courses)
        return finished_courses_str

    # метод сравнения студентов по средней оценке
    def __lt__(self, other):
        # self_avg = self.all_grades_student()
        # other_avg = other.all_grades_student()
        if not isinstance(other, Student):
            print('not a student')
            return
        return self.all_grades_student() < other.all_grades_student()


# КЛАСС ПРЕПОДАВАТЕЛИ
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# КЛАСС ЛЕКТОРЫ
class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}

    # метод рассчета средней оценки лектора
    def all_grades_lector(self):

        list_lector_grades = []
        for course in self.lector_grades:
            list_lector_grades.extend(self.lector_grades[course])

        if len(list_lector_grades) > 0:
            grades_of_lector = round(sum(list_lector_grades) / len(list_lector_grades), 1)
            return grades_of_lector
        else:
            return 'У лектора нет оценок'

    # метод принтования для лектора
    def __str__(self):
        some_lector = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.all_grades_lector()}'
        return some_lector

    # метод сравнения лекторов между собой по средней оценке за лекции
    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Лектор не найден в списке')
            return
        return self.all_grades_lector() < other.all_grades_lector()


# КЛАСС ПРОВЕРЯЮЩИЕ
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # метод оценки студента по конкретному курсy
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]

        else:
            return 'Ошибка'

    # метод принтования для проверяющего
    def __str__(self):
        some_rewiewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_rewiewer


# ЭКЗЕМПЛЯРЫ
# создаем экземпляры класса студентов
student1 = Student('Наталья', 'Куделькина', 'ж')
student1.add_new_course('Python')
student1.add_new_course('GIT')

student2 = Student('Иван', 'Иванов', 'м')
student2.add_new_course('Python')
student2.add_new_course('GIT')

# создаем экземпляры класса лекторов
lector1 = Lector('Анна', 'Петрова')
lector1.courses_attached += ['Python']

lector2 = Lector('Мария', 'Журавлева')
lector2.courses_attached += ['GIT']

# создаем экземпляры класса проверяющих
rewiewer1 = Reviewer('Сергей', 'Сергеев')
rewiewer1.courses_attached += ['Python']

rewiewer2 = Reviewer('Степан', 'Степанов')
rewiewer2.courses_attached += ['GIT']

# РЕАЛИЗУЕМ МЕТОДЫ КЛАССОВ
# Проверяющий 1 оценил студента 1
rewiewer1.rate_hw(student1, 'Python', 10)
# print(student1.grades)


# добавили оцененный курс в завершенные
student1.add_courses('Python')
# print(student1.finished_courses)


# можно сразу удалить по логике курс из текущих (но с ним не реализуется метод выставления оценок)
# student1.delete_course_in_progress('Python')
# print(student1.courses_in_progress)

# проверяющий 2 оценил сстудента 1
rewiewer2.rate_hw(student1, 'GIT', 8)
# print(student1.grades)


student1.add_courses('GIT')
# print(student1.finished_courses)

# student1.delete_course_in_progress('GIT')

# проверяющи1 1 оценил второго студента
rewiewer1.rate_hw(student2, 'Python', 3)
print()
rewiewer2.rate_hw(student2, 'GIT', 8)
# print(student1)
# print()

# print(student2)
# print()

student1.rate_lectors(lector1, 'Python', 9)
student2.rate_lectors(lector1, 'Python', 10)

# print(lector1.lector_grades)

print(lector1)
print()
print(lector2)
print()

student1.rate_lectors(lector2, 'GIT', 7)
student2.rate_lectors(lector2, 'GIT', 6)
print(lector2)
print()
# print(lector2.lector_grades)

# print(student1.all_grades_student())
# print(student2.all_grades_student())
# student1.__lt__(student2)

print(rewiewer1)
print()
print(rewiewer2)
print()

print(student1)
print()

print(student2)
print()

# сравнение студентов
print(student1 > student2)
# сравнение лекторов
print(lector1 > lector2)

# ФУНКЦИИ
# подсчет средней оценки  за ДЗ КУРСА по всем студентам

# print(student1.grades)
# print(student2.grades)

student_list = [student1, student2]


def average_all_students(student_list, course):
    all_grades = []

    for student in student_list:
        if course in student.grades:
            all_grades.extend(student.grades[course])

    if len(all_grades) > 0:
        average_grade_of_some_course = round(sum(all_grades) / len(all_grades), 1)

    else:
        average_grade_of_some_course = 0

    # print(all_grades)
    # print(sum(all_grades))
    # print(len(all_grades))

    print(f'Средняя оценка по всем студентам за {course}:{average_grade_of_some_course}')


average_all_students(student_list, 'GIT')
average_all_students(student_list, 'Python')

# подсчет средней оценки за лекции КУРСА
# для статистики добавила еще одного лектора
lector3 = Lector('Инна', 'Громова')
lector3.courses_attached += ['Python']

student1.rate_lectors(lector3, 'Python', 2)

# print(lector1.lector_grades)
# print(lector3.lector_grades)

lector_list = [lector1, lector2, lector3]


def average_grade_of_course(lector_list, course):
    all_grades = []

    for lector in lector_list:
        if course in lector.lector_grades:
            all_grades.extend(lector.lector_grades[course])

    if len(all_grades) > 0:
        average_grade_of_some_course = round(sum(all_grades) / len(all_grades), 1)

    else:
        average_grade_of_some_course = 0

    # print(all_grades)
    # print(sum(all_grades))
    # print(len(all_grades))

    print(f'Средняя оценка по всем лекторам за {course}:{average_grade_of_some_course}')


print()
average_grade_of_course(lector_list, 'Python')
average_grade_of_course(lector_list, 'GIT')