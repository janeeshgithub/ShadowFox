import csv

# Step 1: Read the CSV file
input_filename = "student_marks.csv"
output_filename = "student_marks_updated.csv"

students = []

with open(input_filename, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ["Total Marks", "Average Marks"]  # Adding new fields

    for row in reader:
        # Convert marks to integers and calculate total and average
        subjects = [int(row[key]) for key in row.keys() if key.startswith("Subject")]
        total_marks = sum(subjects)
        average_marks = total_marks / len(subjects)

        row["Total Marks"] = total_marks
        row["Average Marks"] = round(average_marks, 2)
        students.append(row)

# Step 2: Write the updated data to a new CSV file
with open(output_filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print(f"Updated student marks saved to {output_filename}")
