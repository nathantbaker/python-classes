class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name
    def get_name(self):
        """Returns the name of the company"""
        return self.name

    def add_name(self, name):
        """Returns the name of the company"""
        self.name = name

    def __str__(self):
        return self.name


class Employee(object):

    def __initi__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def get_name(self):
        return self.name

    def add_name(self, name):
        self.name = name

    def __str__(self):
        return "Hi, I'm {}, an employee at the company {}.".format(self.name, my_company)


# Create a class that contains information about employees of a company and define methods to

# get employee name
# set employee name

# get job title
# set job title

# get start date
# set start date

# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# Create a company, and three employees, and then assign the employees to the company.

my_company = Company("Apple")
bruce = Employee()
bruce.add_name("Bruce")
print(bruce)
print("")