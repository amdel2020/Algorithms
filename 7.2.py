class Employee:

    def __init__(self, email):
        self.email = email
        self.free = True


class Respondent(Employee):

    def __init__(self, email):
        Employee.__init__(self, email)


class Manager(Employee):

    def __init__(self, email):
        Employee.__init__(self, email)


class Director(Employee):

    def __init__(self, email):
        Employee.__init__(self, email)


class CallCenter:

    def __init__(self, hierarchy):
        self.employee = {}  # employee is key and level is value
        self.hierarchy = hierarchy  # list of hierarchy

    @staticmethod
    def __assign():
        # iterate over hierarchy
        # check first free employee
        # if found return True
        return False

    def add_employee(self, emp, level):
        self.employee[emp] = level

    def dispatch_call(self):
        return self.__assign()

# Start design with usage of it.
# Is it good for unit test.
# What if I change something.
