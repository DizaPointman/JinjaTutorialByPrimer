# write_messages.py

from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Franz", "score": 69},
    {"name": "Schmebulock", "score": 42},
]

# writing a mesage to every student, depending on grade

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"message_{student['name'].lower()}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )    
    
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... message to {filename}")
        
# putting results into html table

results_filename = "students_results.html"
results_template = environment.get_template("results.html")
# Using context as a name for the collection that stores the variables for a template is a convention
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score
}

with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")
