from sklearn.datasets import fetch_olivetti_faces
import datetime

# Load the dataset
faces = fetch_olivetti_faces()

# Prove that the dataset was loaded
# print(faces.data.shape)

# Only instance methods can access instance attributes. 
# Instance methods are associated with a particular object

class Person:
    # instance attributes
    def __init__(self, name, photo, date_of_birth):
        self.name = name
        self.photo = photo
        self.date_of_birth = date_of_birth

    # instance method
    def get_age(self):
        return int((datetime.datetime.now() - self.date_of_birth).days / 365.25)

    # overriding __str__ built in class method
    def __str__(self):
        return self.name + ', age ' + str(self.get_age())


aPerson = Person("Robert", faces.images[0], datetime.datetime(1998, 10, 21))
print(aPerson.name)

print(str(aPerson.get_age()))

print(str(aPerson))
print(aPerson.__str__())
print(aPerson)


# Inheritance 
class MissingPerson(Person):
    def __init__(self, name, photo, date_of_birth, date_missing):
       # construct the base object
       Person.__init__(self, name, photo, date_of_birth)

       # Add missing_date attribute 
       self.date_missing = date_missing

    #Add get_years_missing() method
    def get_years_missing(self):
        return int((datetime.datetime.now() - self.date_missing).days / 365.25)

missing_person = MissingPerson('Louis', faces.images[1], datetime.datetime(2000, 5, 7), datetime.datetime(2017, 10, 31))
# print(str(missing_person.date_missing))
# print(str(missing_person.get_years_missing()))
print(missing_person.name + ' has been missing for ' + str(missing_person.get_years_missing()) + ' years')

class MissingSKPerson(MissingPerson):
    def __init__(self, name, photo, date_of_birth, date_missing):
        MissingPerson.__init__(self, name, photo, date_of_birth, date_missing)

    # override the get_age() method
    def get_age(self):
        return super().get_age() + 1

name = 'Jung'
faceP = faces.images[2] 
birth = datetime.datetime(1994, 7, 1)
missing = datetime.datetime(2017, 8, 30)

skPerson = MissingSKPerson(name, faceP, birth, missing)
print(skPerson.get_age())

date_birth = datetime.datetime(1990, 9, 16)
date_missing = datetime.datetime(2016, 1, 1)
face = faces.images[0]
name = "Adam"

# Creating Person, MissingPerson & SKMissingPerson objects
aPerson = Person(name, face, date_birth)
print(str(aPerson.get_age()))

aMPerson = MissingPerson(name, face, date_birth, date_missing)
print(str(aPerson.get_age()))

aSKPerson = MissingSKPerson(name, face, date_birth, date_missing)
print(str(aPerson.get_age()))


# Remove an inherited attribute
class AnonymousPerson(Person):
    def __init__(self, photo, date_of_birth):
        Person.__init__(self, '', photo, date_of_birth)
        delattr(self, 'name')

# This cause a runtime error, we can't delete methods
# that are inherited from a base class
# However we can override them and change the way they work    
anonymousPerson = AnonymousPerson(faces.images[4], datetime.datetime(1994, 6, 6))
print(str(anonymousPerson))







