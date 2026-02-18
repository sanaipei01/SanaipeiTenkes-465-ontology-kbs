from kbs import UniversityOntologyKBS

def run_demo():
    kbs = UniversityOntologyKBS()
    
    # 6 Unique Courses
    courses = ["Math101", "Stats201", "ML301", "AI401", "Python101", "DataViz201"]
    for c in courses: kbs.add_course(c)
    
    # 7 Prerequisite Links (Includes 2+ levels of depth)
    kbs.add_prerequisite("Stats201", "Math101")    # Level 1
    kbs.add_prerequisite("ML301", "Stats201")      # Level 2
    kbs.add_prerequisite("AI401", "ML301")         # Level 3
    kbs.add_prerequisite("ML301", "Python101")
    kbs.add_prerequisite("AI401", "Python101")
    kbs.add_prerequisite("DataViz201", "Python101")
    kbs.add_prerequisite("DataViz201", "Stats201")

    # Your 3 Unique Students
    for name in ["Kimani", "Leteipa", "Omondi"]: kbs.add_student(name)

    # Setting up student progress
    kbs.complete_course("Kimani", "Math101")
    kbs.complete_course("Kimani", "Python101")
    kbs.complete_course("Leteipa", "Math101")
    # Omondi starts with nothing

    print("--- 3 ELIGIBILITY CHECKS ---")
    # 1. Eligible
    status, _ = kbs.can_take("Kimani", "Stats201")
    print(f"1. Kimani to Stats201: {'ELIGIBLE' if status else 'NOT ELIGIBLE'}")
    
    # 2. Partially Eligible (Has Math, but missing Python for ML301)
    status, missing = kbs.can_take("Kimani", "ML301")
    print(f"2. Kimani to ML301: {'ELIGIBLE' if status else f'NOT ELIGIBLE (Missing: {missing})'}")
    
    # 3. Not Eligible
    status, missing = kbs.can_take("Omondi", "AI401")
    print(f"3. Omondi to AI401: {'ELIGIBLE' if status else f'NOT ELIGIBLE (Missing: {missing})'}\n")

    print("--- RECOMMENDATIONS ---")
    for s in ["Kimani", "Leteipa", "Omondi"]:
        print(f"{s} is recommended to take: {kbs.recommend_courses(s)}")

if __name__ == "__main__":
    run_demo()
