import json

def generate_report():
    students_list = []

    with open("marks.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()

        if len(parts) == 2:
            name = parts[0]
            marks = int(parts[1])

            if marks >= 70:
                status = "Pass"
            else:
                status = "Fail"

            student = {
                "name": name,
                "marks": marks,
                "status": status
            }
            students_list.append(student)

    report = {
        "students": students_list
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("Report generated successfully!")

generate_report()