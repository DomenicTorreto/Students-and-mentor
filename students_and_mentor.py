class Student:
    def __init__(self, name, surname, gender):
        self.name = str(name)
        self.surname = str(surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __average_grade(self):
        grades = sum(self.grades.values(), [])
        return sum(grades) / len(grades)

    def __str__(self):
        print(f'Имя: {self.name.title()}')
        print(f'Фамилия: {self.surname.title()}')
        print(f"Средняя оценка за домашние задания: {self.__average_grade():.1f}")
        if self.courses_in_progress:
            print(f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}")
        if self.finished_courses:
            print(f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return ""

    def rate_lector(self, lector, course, rating):
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lector_rating:
                lector.lector_rating[course] += [rating]
            else:
                lector.lector_rating[course] = [rating]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__average_grade() < other.__average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = str(name)
        self.surname = str(surname)
        self.courses_attached = []

    def __str__(self):
        print(f'Имя: {self.name.title()}')
        print(f'Фамилия: {self.surname.title()}')
        return ""


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_rating = {}

    def __str__(self):
        Mentor.__str__(self)
        print(f"Средня оценка за лекции: {self.__average_rating():.1f}")
        return ""

    def __average_rating(self):
        rating_list = sum(self.lector_rating.values(), [])
        return sum(rating_list) / len(rating_list)

    def __lt__(self, other):
        if isinstance(other, Lector):
            return self.__average_rating() < other.__average_rating()


def average_lector_rating(course, *args):
    lector_rating_list = []
    lectors_list = args
    for lector in lectors_list:
        if isinstance(lector, Lector) and course in lector.lector_rating:
            lector_rating_list += lector.lector_rating[course]
    return f'Средня оценка лекторов на курсе {course}: {sum(lector_rating_list) / len(lector_rating_list):.1f}'


def average_student_grade(course, *args):
    grade_list = []
    students_list = args
    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            grade_list += student.grades[course]
    return f'Средня оценка студентов на курсе {course}: {sum(grade_list) / len(grade_list):.1f}'


student_ruoy = Student('Ruoy', 'Eman', 'man')
student_ruoy.courses_in_progress += ['Python']
student_ruoy.courses_in_progress += ['Git']
student_ruoy.finished_courses += ['Введение в программирование']

student_alex = Student('Alex', 'Killi', 'man')
student_alex.courses_in_progress += ["Python"]
student_alex.finished_courses += ["Введение в программирование"]

lector_jon = Lector('Jon', 'Glopyn')
lector_jon.courses_attached += ['Python']

lectore_niman = Lector('Niman', 'Hans')
lectore_niman.courses_attached += ['Python']

student_ruoy.rate_lector(lector_jon, 'Python', 9)
student_ruoy.rate_lector(lector_jon, 'Python', 10)
student_ruoy.rate_lector(lector_jon, 'Python', 6)

student_alex.rate_lector(lectore_niman, 'Python', 10)
student_alex.rate_lector(lectore_niman, 'Python', 9)
student_alex.rate_lector(lectore_niman, 'Python', 7)

reviewer_teddi = Reviewer('Teddi', 'Rever')
reviewer_teddi.courses_attached += ['Python']
reviewer_teddi.courses_attached += ['Git']

reviewer_bil = Reviewer('Bil', 'Nepo')
reviewer_bil.courses_attached += ['Python']
reviewer_bil.courses_attached += ['Git']

reviewer_teddi.rate_hw(student_ruoy, 'Python', 8)
reviewer_teddi.rate_hw(student_ruoy, 'Python', 8)
reviewer_teddi.rate_hw(student_ruoy, 'Git', 10)

reviewer_bil.rate_hw(student_alex, 'Python', 8)
reviewer_bil.rate_hw(student_alex, 'Python', 10)
reviewer_bil.rate_hw(student_alex, 'Python', 10)

print(student_alex)
print(student_ruoy)
print(lector_jon)
print(lectore_niman)
print(reviewer_teddi)
print(reviewer_bil)
print(average_lector_rating('Python', lector_jon, lectore_niman))
print(average_student_grade('Git', student_alex, student_ruoy))
print(student_alex < student_ruoy)
print(lector_jon > lectore_niman)
