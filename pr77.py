# attendance_tracker.py

# Input: number of classes held and attended
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate attendance percentage
attendance = (classes_attended / classes_held) * 100

# Display results
print(f"Classes Held: {classes_held}")
print(f"Classes Attended: {classes_attended}")
print(f"Attendance: {attendance:.0f}%")
