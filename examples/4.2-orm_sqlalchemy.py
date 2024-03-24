from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create an SQLite database in memory
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a base class for declarative ORM
Base = declarative_base()

# Define a class representing the department table
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    employees = relationship('Employee', back_populates='department')

    def __repr__(self):
        return f'<Department(id={self.id}, name={self.name})>'

# Define a class representing the employee table
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='employees')

    def __repr__(self):
        return f'<Employee(id={self.id}, name={self.name}, department_id={self.department_id})>'

# Create the database tables based on the ORM classes
Base.metadata.create_all(engine)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Create departments
    department1 = Department(name='Engineering')
    department2 = Department(name='Marketing')

    # Create employees
    employee1 = Employee(name='John Doe', department=department1)
    employee2 = Employee(name='Jane Smith', department=department2)
    employee3 = Employee(name='Bob Johnson', department=department1)

    # Add departments and employees to the session and commit
    session.add_all([department1, department2, employee1, employee2, employee3])
    session.commit()

    # Query the database for all employees and print their details with department information
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"{employee.name} works in the {employee.department.name} department")
