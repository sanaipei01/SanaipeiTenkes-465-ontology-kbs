# SanaipeiTenkes-465-ontology-kbs

## Project Description
A Knowledge-Based System (KBS) that models a University Advising Ontology. It uses logical inference to determine student eligibility for courses based on prerequisites and provides sorted recommendations.

## Ontology Design
- **Concepts (Classes):** Student, Course.
- **Relationships (Properties):** - `requires(Course -> Course)`: Defines prerequisites.
  - `completed(Student -> Course)`: Tracks student progress.
  - `eligibleFor(Student -> Course)`: Inferred relationship.

## Inference Logic
The system uses **Set-Difference Inference**. To determine if a student is `eligibleFor` a course, the system calculates:
`Missing = (Prerequisites of Course) - (Courses completed by Student)`
If the set is empty, the student is eligible.

## How to Run
1. Run the demo: `python demo.py`
2. Run unit tests: `python -m unittest tests/test_kbs.py`

## Example Output
Kimani to Stats201: ELIGIBLE
Leteipa is recommended to take: ['Math101', 'Python101']