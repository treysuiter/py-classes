# Practice: Companies and Employees
# Setup
# mkdir -p ~/workspace/python/exercises/classes && cd $_
# touch employees_departments.py
# Instructions
# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
# Create two companies, and 5 people who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras

class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


class Company:
    def __init__(self, name, address, industryType):
        self.name = name
        self.address = address
        self.industryType = industryType
        self.employees = []

    def print_employees(self):
        for employee in self.employees:
            print(f"* {employee.name}")

jen_makeItSmaller = Company("Jen's Make Things Smaller Shop", "100 Street St,", "Professional Shrinking")
bob_makeItBigger = Company("Bob's Make It Bigger Shop", "200 Street St.", "Professional Enlargement")

jimEmp = Employee("Jimmy Jam", "Ratio Manipulator", "01/02/2001")
philEmp = Employee("Phil Duck", "Size Analyst", "01/03/2001")
gilEmp = Employee("Gil Gurper", "Measurement Consultant", "01/04/2001")
jilEmp = Employee("Jil Jones", "Protractor Contractor", "01/05/2001")
rockEmp = Employee("Rock Roll", "Non-Stop Rocker", "01/06/2001")

jen_makeItSmaller.employees.append(jimEmp)
jen_makeItSmaller.employees.append(philEmp)

bob_makeItBigger.employees.append(gilEmp)
bob_makeItBigger.employees.append(jilEmp)
bob_makeItBigger.employees.append(rockEmp)

allCompanies = [jen_makeItSmaller, bob_makeItBigger]
    
for company in allCompanies:

    print(f"{company.name} is in the {company.industryType} business and has the following employyes:")
    print()
    company.print_employees()
    print()
