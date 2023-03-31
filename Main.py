from LibraryStaff import LibraryStaff

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

    print(libraryStaff.years_on_job())

    print(libraryStaff.age())

    print(libraryStaff.years_to_retire())

if __name__ == "__main__":
    main()