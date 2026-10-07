import streamlit as st

# -----------------------------
# Student Data
# -----------------------------

students = {
    "ST001": {
        "name": "Arun",
        "age": 20,
        "department": "AI & ML",
        "year": 2,
        "marks": 85
    },
    "ST002": {
        "name": "Priya",
        "age": 19,
        "department": "Computer Science",
        "year": 2,
        "marks": 90
    },
    "ST003": {
        "name": "Rahul",
        "age": 21,
        "department": "Information Technology",
        "year": 3,
        "marks": 78
    },
    "ST004": {
        "name": "Divya",
        "age": 20,
        "department": "Electronics",
        "year": 2,
        "marks": 88
    },
    "ST005": {
        "name": "Karthik",
        "age": 21,
        "department": "AI & ML",
        "year": 3,
        "marks": 92
    }
}


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Student Information Dictionary",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🎓 Student Information Dictionary")

st.write(
    "A Python-based student record management system "
    "using dictionaries."
)

st.divider()


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📌 Operations")

operation = st.sidebar.selectbox(
    "Choose an operation",
    [
        "View All Students",
        "Search Student",
        "Add Student",
        "Update Student",
        "Student Statistics"
    ]
)


# -----------------------------
# View All Students
# -----------------------------

if operation == "View All Students":

    st.header("📋 All Student Records")

    for student_id, details in students.items():

        with st.expander(
            f"{student_id} - {details['name']}"
        ):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("**Age:**", details["age"])
                st.write("**Year:**", details["year"])

            with col2:
                st.write(
                    "**Department:**",
                    details["department"]
                )

            with col3:
                st.write(
                    "**Marks:**",
                    details["marks"]
                )


# -----------------------------
# Search Student
# -----------------------------

elif operation == "Search Student":

    st.header("🔍 Search Student")

    student_id = st.text_input(
        "Enter Student ID",
        placeholder="Example: ST001"
    )

    if st.button("Search Student"):

        if student_id in students:

            student = students[student_id]

            st.success("Student Found!")

            st.write("### Student Information")

            st.write("**Student ID:**", student_id)
            st.write("**Name:**", student["name"])
            st.write("**Age:**", student["age"])
            st.write(
                "**Department:**",
                student["department"]
            )
            st.write("**Year:**", student["year"])
            st.write("**Marks:**", student["marks"])

        else:

            st.error("Student not found.")


# -----------------------------
# Add Student
# -----------------------------

elif operation == "Add Student":

    st.header("➕ Add New Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=20
    )

    department = st.text_input("Department")

    year = st.number_input(
        "Year",
        min_value=1,
        max_value=5,
        value=1
    )

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        value=50
    )

    if st.button("Add Student"):

        if student_id in students:

            st.error(
                "Student ID already exists."
            )

        elif student_id == "":

            st.warning(
                "Please enter a Student ID."
            )

        else:

            students[student_id] = {
                "name": name,
                "age": age,
                "department": department,
                "year": year,
                "marks": marks
            }

            st.success(
                "Student added successfully!"
            )


# -----------------------------
# Update Student
# -----------------------------

elif operation == "Update Student":

    st.header("✏️ Update Student")

    student_id = st.text_input(
        "Enter Student ID"
    )

    if student_id in students:

        student = students[student_id]

        name = st.text_input(
            "Name",
            value=student["name"]
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=student["age"]
        )

        department = st.text_input(
            "Department",
            value=student["department"]
        )

        year = st.number_input(
            "Year",
            min_value=1,
            max_value=5,
            value=student["year"]
        )

        marks = st.number_input(
            "Marks",
            min_value=0,
            max_value=100,
            value=student["marks"]
        )

        if st.button("Update Student"):

            students[student_id] = {
                "name": name,
                "age": age,
                "department": department,
                "year": year,
                "marks": marks
            }

            st.success(
                "Student information updated successfully!"
            )

    elif student_id != "":

        st.error("Student not found.")


# -----------------------------
# Statistics
# -----------------------------

elif operation == "Student Statistics":

    st.header("📊 Student Statistics")

    total_students = len(students)

    total_marks = sum(
        student["marks"]
        for student in students.values()
    )

    average_marks = (
        total_marks / total_students
        if total_students > 0
        else 0
    )

    top_student_id = max(
        students,
        key=lambda x: students[x]["marks"]
    )

    top_student = students[top_student_id]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Students",
            total_students
        )

    with col2:
        st.metric(
            "Average Marks",
            f"{average_marks:.2f}"
        )

    with col3:
        st.metric(
            "Top Marks",
            top_student["marks"]
        )

    st.divider()

    st.subheader("🏆 Top Student")

    st.write(
        "**Student ID:**",
        top_student_id
    )

    st.write(
        "**Name:**",
        top_student["name"]
    )

    st.write(
        "**Marks:**",
        top_student["marks"]
    )