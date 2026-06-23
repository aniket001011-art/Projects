import matplotlib.pyplot as plt

# Data
students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 90, 66, 88]
attendance = [90, 85, 95, 80, 92]

# ------------------ Line Chart ------------------
plt.figure(figsize=(5,4))
plt.title("Line Chart for Marks")
plt.plot(students, marks, 'or--')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.savefig("images/line_chart.png")
plt.close()

# ------------------ Bar Chart ------------------
plt.figure(figsize=(5,4))
plt.title("Bar Chart for Attendance")
plt.bar(students, attendance, color='g')
plt.xlabel("Students")
plt.ylabel("Attendance")
plt.savefig("images/bar_chart.png")
plt.close()

# ------------------ Scatter Plot ------------------
plt.figure(figsize=(5,4))
plt.title("Scatter Plot for Marks")
plt.scatter(students, marks, color='m')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.savefig("images/scatter_chart.png")
plt.close()

# ------------------ Pie Chart ------------------
plt.figure(figsize=(5,4))
plt.title("Pie Chart Showing Marks Percentage")
plt.pie(marks, labels=students, autopct="%1.1f%%", startangle=90)
plt.savefig("images/pie_chart.png")
plt.close()

print("All charts have been saved successfully!")