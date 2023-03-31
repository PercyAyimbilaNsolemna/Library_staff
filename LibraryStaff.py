import datetime

class LibraryStaff:
    def __init__(self, full_name=None, year_of_employment=None, staffID=None, rank=None, gender=None, department=None, salary=None, year_of_birth=None, awards=None, sanctions=None, city=None, region=None):
        self.full_name = full_name
        self.year_of_employment = year_of_employment
        self.staffID = staffID
        self.rank = rank
        self.gender = gender
        self.department = department
        self.salary = salary
        self.year_of_birth = year_of_birth
        self.awards = awards
        self.sanctions = sanctions
        self.city = city
        self.region = region

    def __str__(self):
        return "This is a libary staff class"
    
    #Creates a method to check the number of years the employess has been in the job
    def years_on_job(self):
        

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name
    
    @property 
    def year_of_employment(self):
        return self._year_of_employment


    @year_of_employment.setter
    def year_of_employment(self, year_of_employment):
        self._year_of_employment = year_of_employment
    
    @property
    def staffID(self):
        return self._staffID

    @staffID.setter
    def staffID(self, staffID):
        self._staffID = staffID

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
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
    
    @property
    def year_of_birth(self):
        return self._year_of_birth
    
    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self._year_of_birth = year_of_birth

    @property
    def awards(self):
        return self._awards
    
    @awards.setter
    def awards(self, awards):
        self._awards = awards
    
    @property
    def sanctions(self):
        return self._sanctions

    @sanctions.setter
    def sanctions(self, sanctions):
        self._sanctions = sanctions

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
 

def main():
    libraryStaff = LibraryStaff()
    print(libraryStaff)

    libraryStaff.full_name = "Dennis Agbo"
    print(f"Full name of staff: {libraryStaff.full_name}")

    libraryStaff.year_of_employment = 2019
    print(f"Staff year of employment: {libraryStaff.year_of_employment}")

    libraryStaff.staffID = "10239855"
    print(f"{libraryStaff.full_name}'s staff ID: {libraryStaff.staffID}")

    libraryStaff.rank = "Secretary"
    print(f"{libraryStaff.full_name}'s rank: {libraryStaff.rank}")

    libraryStaff.gender = "Male"
    print(f"Gender: {libraryStaff.gender}")

    libraryStaff.department = "CS"
    print(f"Department: {libraryStaff.department}")

    libraryStaff.salary = 2300
    print(f"{libraryStaff.full_name}'s salary: ${libraryStaff.salary}")

    libraryStaff.year_of_birth = "2006"
    print(f"{libraryStaff.full_name}'s year of birth: {libraryStaff.year_of_birth}")

    libraryStaff.awards = "Best librarian of the year"
    print(f"{libraryStaff.full_name}'s award: {libraryStaff.awards}")

    libraryStaff.sanctions = "No sanctions"
    print(f"{libraryStaff.full_name} sanctions: {libraryStaff.sanctions}")

    libraryStaff.city = "Accra"
    print(f"{libraryStaff.full_name}'s city: {libraryStaff.city}")

    libraryStaff.region = "Greater Accra"
    print(f"{libraryStaff.full_name}'s region: {libraryStaff.region}")

if __name__ == "__main__":
    main()