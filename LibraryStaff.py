class LibraryStaff:
    def __init__(self, full_name=None, year_of_employment=None, staffID=None, rank=None, gender=None, department=None, salary=None, year_of_birth=None, sanctions=None, city=None, region=None):
        self.full_name = full_name
        self.year_of_employment = year_of_employment
        self.staffID = staff_ID
        self.rank = rank
        self.gender = gender
        self.department = department
        self.salary = salary
        self.year_of_birth = year_of_birth
        self.sanctions = sanctions
        self.city = city
        self.region = region

    def __str__(self):
    return "This is a libary staff class"

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name

    @property 
    def rank(self):
        return self._rank
 
    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def region(self):
        return self._region  

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def sanctions(self):
        return self.sanctions

    @sanctions.setter
    def sanctions(self, sanctions):
        self._sanctions = sanctions


    @property 
    def year_of_employment(self):
        return self._year_of_employment


    @year_of_employment.setter
    def year_of_employment(self, year_of_employment):
        self._year_of_employment = year_of_employment

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department