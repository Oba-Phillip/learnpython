"""
University System Implementation
Contains Person base class and Student, Lecturer, Staff subclasses
Includes test cases for all classes
"""

class Person:
    def __init__(self, name, age, email):
        """
        Initialize a Person with basic information
        
        Args:
            name (str): Full name of the person
            age (int): Age of the person
            email (str): Email address of the person
        """
        self.name = name
        self.age = age
        self.email = email
        self.role = "Generic Person"
    
    def display_info(self):
        """Display basic information about the person"""
        info = f"""
        {self.role} Information:
        Name: {self.name}
        Age: {self.age}
        Email: {self.email}
        """
        print(info)
    
    def __str__(self):
        return f"{self.role}: {self.name} ({self.age})"


class Student(Person):
    def __init__(self, name, age, email, student_id, major, year):
        """
        Initialize a Student with academic information
        
        Args:
            student_id (str): Unique student identifier
            major (str): Student's major field of study
            year (int): Year of study (1-4)
        """
        super().__init__(name, age, email)
        self.student_id = student_id
        self.major = major
        self.year = year
        self.courses = []
        self.role = "Student"
    
    def enroll_course(self, course_code):
        """Enroll student in a new course"""
        if course_code not in self.courses:
            self.courses.append(course_code)
            return f"Enrolled in {course_code}"
        return f"Already enrolled in {course_code}"
    
    def display_info(self):
        """Display student information including academic details"""
        super().display_info()
        academic_info = f"""
        Academic Information:
        Student ID: {self.student_id}
        Major: {self.major}
        Year: {self.year}
        Courses: {', '.join(self.courses) if self.courses else 'None'}
        """
        print(academic_info)
    
    def __str__(self):
        return f"{super().__str__()} | Major: {self.major}"


class Lecturer(Person):
    def __init__(self, name, age, email, employee_id, department, courses_taught):
        """
        Initialize a Lecturer with professional information
        
        Args:
            employee_id (str): Unique employee identifier
            department (str): Academic department
            courses_taught (list): List of course codes the lecturer teaches
        """
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.courses_taught = courses_taught
        self.office_hours = []
        self.role = "Lecturer"
    
    def add_office_hours(self, day, time):
        """Add office hours for the lecturer"""
        self.office_hours.append((day, time))
        return f"Added office hours: {day} at {time}"
    
    def display_info(self):
        """Display lecturer information including professional details"""
        super().display_info()
        professional_info = f"""
        Professional Information:
        Employee ID: {self.employee_id}
        Department: {self.department}
        Courses Taught: {', '.join(self.courses_taught)}
        Office Hours: {', '.join([f'{day} {time}' for day, time in self.office_hours]) if self.office_hours else 'None'}
        """
        print(professional_info)
    
    def __str__(self):
        return f"{super().__str__()} | Department: {self.department}"


class Staff(Person):
    def __init__(self, name, age, email, employee_id, position, department):
        """
        Initialize a Staff member with professional information
        
        Args:
            employee_id (str): Unique employee identifier
            position (str): Job position/title
            department (str): Administrative department
        """
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.position = position
        self.department = department
        self.role = "Staff Member"
    
    def update_position(self, new_position):
        """Update the staff member's position"""
        self.position = new_position
        return f"Position updated to: {new_position}"
    
    def display_info(self):
        """Display staff information including professional details"""
        super().display_info()
        professional_info = f"""
        Professional Information:
        Employee ID: {self.employee_id}
        Position: {self.position}
        Department: {self.department}
        """
        print(professional_info)
    
    def __str__(self):
        return f"{super().__str__()} | Position: {self.position}"


def demonstrate_system():
    """Demonstrate the university system functionality"""
    print("\nUniversity System Demonstration")
    print("=" * 50 + "\n")
    
    # Create instances
    student = Student(
        name="Alice Johnson",
        age=20,
        email="alice.johnson@university.edu",
        student_id="S10001",
        major="Computer Science",
        year=2
    )
    
    lecturer = Lecturer(
        name="Dr. Robert Smith",
        age=45,
        email="r.smith@university.edu",
        employee_id="L20001",
        department="Computer Science",
        courses_taught=["CS101", "CS202", "CS305"]
    )
    
    staff = Staff(
        name="Emma Wilson",
        age=32,
        email="e.wilson@university.edu",
        employee_id="ST30001",
        position="Administrative Assistant",
        department="Registrar's Office"
    )
    
    # Demonstrate functionality
    print("Student Operations:")
    print(student.enroll_course("CS101"))
    print(student.enroll_course("MATH201"))
    print(student.enroll_course("CS101"))  # Try duplicate enrollment
    print()
    
    print("Lecturer Operations:")
    print(lecturer.add_office_hours("Monday", "2:00 PM - 4:00 PM"))
    print(lecturer.add_office_hours("Wednesday", "10:00 AM - 12:00 PM"))
    print()
    
    print("Staff Operations:")
    print(staff.update_position("Senior Administrative Assistant"))
    print()
    
    # Display information
    print("Student Information:")
    student.display_info()
    
    print("\nLecturer Information:")
    lecturer.display_info()
    
    print("\nStaff Information:")
    staff.display_info()


# Test Cases
import unittest

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John Doe", 30, "john.doe@example.com")
    
    def test_initialization(self):
        self.assertEqual(self.person.name, "John Doe")
        self.assertEqual(self.person.age, 30)
        self.assertEqual(self.person.email, "john.doe@example.com")
        self.assertEqual(self.person.role, "Generic Person")
    
    def test_display_info(self):
        # This just tests that the method runs without errors
        self.assertIsNone(self.person.display_info())
    
    def test_str_representation(self):
        self.assertEqual(str(self.person), "Generic Person: John Doe (30)")


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(
            "Alice Johnson", 20, "alice@uni.edu", 
            "S10001", "Computer Science", 2
        )
    
    def test_initialization(self):
        self.assertEqual(self.student.name, "Alice Johnson")
        self.assertEqual(self.student.student_id, "S10001")
        self.assertEqual(self.student.major, "Computer Science")
        self.assertEqual(self.student.year, 2)
        self.assertEqual(self.student.role, "Student")
        self.assertEqual(self.student.courses, [])
    
    def test_enroll_course(self):
        result = self.student.enroll_course("CS101")
        self.assertEqual(result, "Enrolled in CS101")
        self.assertIn("CS101", self.student.courses)
        
        # Test duplicate enrollment
        result = self.student.enroll_course("CS101")
        self.assertEqual(result, "Already enrolled in CS101")
    
    def test_display_info(self):
        # Just test that it runs without errors
        self.assertIsNone(self.student.display_info())


class TestLecturer(unittest.TestCase):
    def setUp(self):
        self.lecturer = Lecturer(
            "Dr. Smith", 45, "smith@uni.edu",
            "L20001", "Computer Science", ["CS101", "CS202"]
        )
    
    def test_initialization(self):
        self.assertEqual(self.lecturer.name, "Dr. Smith")
        self.assertEqual(self.lecturer.employee_id, "L20001")
        self.assertEqual(self.lecturer.department, "Computer Science")
        self.assertEqual(self.lecturer.courses_taught, ["CS101", "CS202"])
        self.assertEqual(self.lecturer.role, "Lecturer")
        self.assertEqual(self.lecturer.office_hours, [])
    
    def test_add_office_hours(self):
        result = self.lecturer.add_office_hours("Monday", "2-4 PM")
        self.assertEqual(result, "Added office hours: Monday at 2-4 PM")
        self.assertIn(("Monday", "2-4 PM"), self.lecturer.office_hours)
    
    def test_display_info(self):
        # Just test that it runs without errors
        self.assertIsNone(self.lecturer.display_info())


class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff(
            "Emma Wilson", 35, "emma@uni.edu",
            "ST30001", "Administrator", "Registrar's Office"
        )
    
    def test_initialization(self):
        self.assertEqual(self.staff.name, "Emma Wilson")
        self.assertEqual(self.staff.employee_id, "ST30001")
        self.assertEqual(self.staff.position, "Administrator")
        self.assertEqual(self.staff.department, "Registrar's Office")
        self.assertEqual(self.staff.role, "Staff Member")
    
    def test_update_position(self):
        result = self.staff.update_position("Senior Administrator")
        self.assertEqual(result, "Position updated to: Senior Administrator")
        self.assertEqual(self.staff.position, "Senior Administrator")
    
    def test_display_info(self):
        # Just test that it runs without errors
        self.assertIsNone(self.staff.display_info())


if __name__ == "__main__":
    # Run demonstration
    demonstrate_system()
    
    # Run tests
    print("\n" + "=" * 50)
    print("Running Tests...")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)