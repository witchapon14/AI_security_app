import streamlit as st
# ตั้งค่าแสดงผลเป็นหน้าหลัก
st.title("# Meet Our Team 👾")

# ตั้งค่าให้ Sidebar สามารถเลือก Demo ต่าง ๆ ได้
st.sidebar.success("Select a demo above.")

# สร้างข้อมูลเพื่อนในทีม (ชื่อ, รูปภาพ, อายุ, งาน, รหัสนักศึกษา)
team_members = [
    {
        "name": "Witchapon Kasettakarn", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 25, 
        "job": "Network Security Engineer", 
        "student_id": "S1234567"
    },
    {
        "name": "Wasan Boonsong", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 30, 
        "job": "Cybersecurity Analyst", 
        "student_id": "S7654321"
    },
    {
        "name": "Charlie Brown", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 28, 
        "job": "Ethical Hacker", 
        "student_id": "S9876543"
    }
]

# แสดงข้อมูลเพื่อนในทีม
for member in team_members:
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{member['image']}" alt="{member['name']}" style="width: 300px;">
            <h3 style='color: #00FF00;'>{member['name']}</h3>
            <p style='color: white;'>
                <b>Age:</b> {member['age']}<br>
                <b>Job:</b> {member['job']}<br>
                <b>Student ID:</b> {member['student_id']}
            </p>
        </div>
        <hr style='border-top: 3px solid #00FF00;'>
    """, unsafe_allow_html=True)

# ตั้งค่าธีม Cyber Security โดยใช้ CSS
st.markdown("""
    <style>
    .reportview-container {
        background: #1E1E1E;
        color: white;
    }
    h3 {
        font-family: 'Courier New', monospace;
        text-align: center;
    }
    p {
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    hr {
        border-top: 2px solid #00FF00;
    }
    </style>
    """, unsafe_allow_html=True)