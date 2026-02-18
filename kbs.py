class UniversityOntologyKBS:
    def __init__(self):
        self.students = {}  # {name: set(completed_courses)}
        self.courses = set()
        self.prerequisites = {} # {course: set(prereqs)}

    def add_student(self, student: str):
        if not student: raise ValueError("Name cannot be empty")
        self.students[student] = set()

    def add_course(self, course: str):
        self.courses.add(course)
        if course not in self.prerequisites:
            self.prerequisites[course] = set()

    def add_prerequisite(self, course: str, prereq: str):
        if course not in self.courses or prereq not in self.courses:
            raise ValueError("Course or Prerequisite not found in system.")
        self.prerequisites[course].add(prereq)

    def complete_course(self, student: str, course: str):
        if student not in self.students:
            raise ValueError(f"Student {student} not found.")
        self.students[student].add(course)

    def can_take(self, student: str, course: str) -> tuple[bool, set[str]]:
        if student not in self.students or course not in self.courses:
            raise ValueError("Invalid student or course name.")
        
        required = self.prerequisites.get(course, set())
        completed = self.students[student]
        missing = required - completed
        
        return (len(missing) == 0, missing)

    def recommend_courses(self, student: str) -> list[str]:
        if student not in self.students:
            raise ValueError("Student not found.")
        
        recommendations = []
        completed = self.students[student]
        
        for c in self.courses:
            if c not in completed:
                eligible, _ = self.can_take(student, c)
                if eligible:
                    recommendations.append(c)
        return sorted(recommendations)
