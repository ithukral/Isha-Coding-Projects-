# HW2
#Due Date: 02/20/2021, 11:59PM
# Isha Thukral
"""                                   
### Collaboration Statement: Worked on with TA
             
"""

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid #stores the id, name, and number of credits for a class.
        self.cname = cname
        self.credits = credits


    def __str__(self):
        # YOUR CODE STARTS HERE
        #Returns a formatted summary
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE # c2 = 2
        #Determines if two objects are equal.
        if isinstance(other,Course):
            if self.cid == other.cid:
                return True
            else:
                return False
        else:
            return False


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''
    def __init__(self):
        # YOUR CODE STARTS HERE
        #stores collection of courses as dictionary
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #stores it as a value in courseOfferings
        if cid in self.courseOfferings:
            return 'Course already added'
        else:
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return 'Course added successfully'


    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        #Removes a course with the given id.
        if cid not in self.courseOfferings:
            return 'Course not found'
        else:
            self.courseOfferings.pop(cid)
            return 'Course removed successfully'
            
  

class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        #stores collection of course objects for semester for student
        self.sem_num = sem_num
        self.courses = []


    def __str__(self):
        # YOUR CODE STARTS HERE
        # Returns a formatted summary of the all the courses in this semester.
        # format: cid, cid, cid,
        if self.courses == []:
            return 'No courses'
        output = ''
        for i in range(len(self.courses)):
            if i != (len(self.courses) - 1):
                output += self.courses[i].cid + ', '
            else:
                output += self.courses[i].cid
        return output 

    __repr__ = __str__

    def valid(self, course):
        #checks the type for each object to make sure valid
        return type(course.cid) == str and type(course.cname) == str and type(course.credits) == int
    

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        # Adds a course to courses if it is a valid course object.
        if not isinstance(course, Course) or not self.valid(course): #check type 
            return 'Invalid course'
        elif course in self.courses:
            return 'Course already added'
        else:
            self.courses.append(course)

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        # Removes a course from this semester.
        if not isinstance(course, Course) or not self.valid(course): # check valid as well calling the function
            return 'Invalid course'
        elif course not in self.courses:
            return 'No such course'
        else:
            self.courses.remove(course)

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        # total number of credits in this semester.
        totalcredits = 0
        for course in self.courses:
            totalcredits += course.credits # add update
        return totalcredits

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        # checks if a student taking this semester would be considered full-time (taking 12 or more credits) or not.
        if self.totalCredits >= 12:
            return True
        else:
            return False

    
class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        # class that represents an amount of money
        # use __ to make a private attribute 
        self.loan_id = self.__loanID
        self.amount = amount 


    def __str__(self):
        # YOUR CODE STARTS HERE
        # Use the format: Balance: $amount
        return f"Balance: ${self.amount}"

    __repr__ = __str__


    @property
    def __loanID(self):
        # YOUR CODE STARTS HERE
        # uses random method to generate number between the two
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        # representation of a person, storing name and social security number
        self.name = name
        self.__ssn = ssn
    
    def __str__(self):
        # YOUR CODE STARTS HERE
        # The format to use is: Person(name, ***-**-last four digits)
        # uses -4 to access the last four
        # create a new variable to input it in 
        temp_ssn = self.__ssn[-4:]
        return f"Person({self.name}, ***-**-{temp_ssn})" 

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        # accessing the private social security number attribute.
        return self.__ssn 

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        # checks type than determines if equal or not 
        if type(other) == Person:
            if self.__ssn == other.__ssn:
                return True
            else:
                return False
        else:
            return False 

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE 
        # staff(name,ssn)
        # staff(name,ssn,supervisor)
        # s1.name
        # inherits from the Person class but adds extended functionality for staff members. 
        super().__init__(name,ssn)
        self.__supervisor = supervisor


    def __str__(self):
        # YOUR CODE STARTS HERE
        # format to use is: Staff(name, id)
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        # 905+initials+last four numbers of ssn.
        # using the for loop we are able to break up first and last name and retrieve the intial
        initials = ''
        for n in self.name.split(' '):
            initials += n[0]
        initials = initials.lower()

        return '905'+initials+self.get_ssn()[-4:]

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        # Updates the private supervisor attribute
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        # for getting the supervisor.
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor
            return "Completed!"
        else:
            return None

    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        # using the hold method defined later in the code
        if isinstance(student, Student):
            student.hold = True
            return 'Completed!'
        else:
            return None

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        # using the boolean able to figure out if hold or not 
        if isinstance(student, Student):
            student.hold = False
            return 'Completed!'
        else:
            return None

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        # Unerrol student object
        # using .active defined later in the code
        if isinstance(student, Student):
            student.active = False
            return 'Completed!'
        else:
            return None



class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        # inherits from the Person class and is heavy extended for additional functionality
        self.year = year
        self.semesters = {} # key : sem_num value:Semester(sem_num)
        self.hold = False
        self.active = True 
        self.account = self.__createStudentAccount()
        super().__init__(name,ssn)

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.year})"

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        # Created StudentAccount object linked to the student.
        if self.active:
            return StudentAccount(self)
        else:
            return None


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        # initials+last four numbers of ssn 
        # using the previous funtion created
        initials = ''
        for n in self.name.split(' '):
            initials += n[0]
        initials = initials.lower()

        return initials+self.get_ssn()[-4:]

    def registerSemester(self):
        # YOUR CODE STARTS HERE 
        # assigns the students level using <= 
        # updates the self.year
        if self.active and (not self.hold):
            sem_no = len(self.semesters)
            self.semesters[sem_no+1] = Semester(sem_no+1)
            if sem_no+1 <= 2:
                self.year = 'Freshman'
            elif sem_no+1 <= 4:
                self.year = 'Sophomore'
            elif sem_no+1 <= 6:
                self.year = 'Junior'
            else:
                self.year = 'Senior'
        else:
            return 'Unsuccessful operation'



    def enrollCourse(self, cid, catalog, semester):
        # YOUR CODE STARTS HERE
        # adds it to the courses attribute of the Semester object. 
        # charges the student 1000 times the quantity 
        # using the if statments to see if course qualifies
        if self.active and (not self.hold):
            if not semester in self.semesters:
                return 'Invalid Semester'
            else:
                if not cid in catalog.courseOfferings:
                    return 'Course not found'
                if catalog.courseOfferings[cid] in self.semesters[semester].courses:
                    return 'Course already enrolled'

                self.semesters[semester].addCourse(catalog.courseOfferings[cid])
                self.account.chargeAccount(StudentAccount.CREDIT_PRICE*catalog.courseOfferings[cid].credits) 
                return 'Course added successfully'

        else:
            return "Unsuccessful operation"


    def dropCourse(self, cid, semester):
        # YOUR CODE STARTS HERE
        # Course object from the specified semester with the given id and removes it
        # creates size and looks at the length of the courses
        # no money is refunded to the student’s account hence same logic 
        if self.active and (not self.hold):
            if not semester in self.semesters:
                return 'Invalid Semester'
            else:
                size = len(self.semesters[semester].courses) # 10
                if size == 0:
                    return 'Course not found'
                
                for i in range(size):
                    if self.semesters[semester].courses[i].cid == cid:
                        self.account.makePayment(StudentAccount.CREDIT_PRICE*self.semesters[semester].courses[i].credits)
                        self.semesters[semester].courses.pop(i)  #9
                        return 'Course dropped successfully'

                if len(self.semesters[semester].courses) == size:
                    return 'Course not found'
        else:
            return "Unsuccessful operation"

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        # Loan object for the student with the given amount, adds
        # uses the amount to make a payment in the student’s account
        if self.active and (not self.hold):
            sem_no = len(self.semesters) # 0 -> {} -> finding zero returns an error
            if sem_no == 0 or (self.semesters[sem_no] is None):  # as one is true it won't check other
                return 'Not full-time'
            if self.semesters[sem_no].isFullTime :
                loan_obj = Loan(amount)
                self.account.loans[loan_obj.loan_id] = loan_obj
                self.account.makePayment(amount)
            else:
                return 'Not full-time'



class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
    '''
    CREDIT_PRICE  = 1000
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        # class represents a financial status of the student based on enrollment and is saved to a Student
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        # YOUR CODE STARTS HERE
        #\n to put on new line
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        # updates by subtracting balance
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        # adding to balance
        self.balance += amount
        return self.balance




####################### STAND ALONE FUNCTION ###############################################


def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    # new student info and label as freshmen
    return Student(person.name, person.get_ssn(), 'Freshman')


#if __name__ == '___main__':
    #import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(Course,globals,name='HW2',verbose=True)