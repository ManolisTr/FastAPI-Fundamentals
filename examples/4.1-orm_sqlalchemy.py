from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database in memory
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a base class for declarative ORM
Base = declarative_base()

# Define a class representing the employee table
class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)

    # In Python, __repr__ is a special method used to represent a class’s objects as a string. 
    def __repr__(self):
        return f'<Employee(id={self.id}, name={self.name}, department={self.department})>'

# Create the database tables based on the ORM classes
Base.metadata.create_all(engine)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Create some employees and add them to the database
    employee1 = Employee(name='John Doe', department='Engineering')
    employee2 = Employee(name='Jane Smith', department='Marketing')
    employee3 = Employee(name='Bob Johnson', department='HR')

    session.add_all([employee1, employee2, employee3])
    session.commit()

    # Query the database for all employees and print their details
    employees = session.query(Employee).all()
    for employee in employees:
        print(employee)
