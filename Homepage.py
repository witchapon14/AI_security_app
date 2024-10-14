import streamlit as st
# ตั้งค่าแสดงผลเป็นหน้าหลัก
st.title("# Meet Our Team 👾")

# ตั้งค่าให้ Sidebar สามารถเลือก Demo ต่าง ๆ ได้
st.sidebar.success("Select a demo above.")

# สร้างข้อมูลเพื่อนในทีม (ชื่อ, รูปภาพ, อายุ, งาน, รหัสนักศึกษา)
team_members = [
    {
        "name": "วิชญ์พล เกษตรตระการ", 
        "image": "https://scontent.fbkk7-2.fna.fbcdn.net/v/t39.30808-6/432734685_2484109161762017_8950146803975549470_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeFpCo_IXvuKaLClPRVUoRYsaCnGC3SrnCJoKcYLdKucInQwLUQaPCYcKROFuZQ-bLJBb42tzr-fG9moxyqmpmy7&_nc_ohc=9fQrLDHyuI8Q7kNvgFClhoh&_nc_ht=scontent.fbkk7-2.fna&_nc_gid=AqbOYq9DW_8kM4vAQCAc_7w&oh=00_AYDw4AHyZ2y0g-_90FoJZiX0FvSbYRzMTzZ3C8j1fuV2ig&oe=6712ACB2", 
        "age": 20, 
        "student_id": "65010986"
    },
    {
        "name": "สุรพิชญ์ เทียบข่วง", 
        "image": "https://www.iote.kmitl.ac.th/wp-content/uploads/2024/09/33629-2-173x300.jpg", 
        "age": 20, 
        "student_id": "65011146"
    },
    {
        "name": "ภัทรชนน เมธาวุฒิยาภรณ์", 
        "image": "https://scontent.fbkk7-2.fna.fbcdn.net/v/t39.30808-6/438037450_1934093420393949_5737898906754750950_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeEvYDcMQ6ydqqShmDSTLbgUFI3i6ypynBgUjeLrKnKcGIY_hnW1joZITXMfGNAvoKPiGrZkBr4xAKuGz3nsrJUV&_nc_ohc=l9IzzW_YJTEQ7kNvgFRGyCQ&_nc_ht=scontent.fbkk7-2.fna&_nc_gid=AfOLDEAdEkgJ8IKUSzvr4c2&oh=00_AYC4FZnWu2E0AlHi2y-hpapobVB7j3UxtUgHYtyZWaLJ1g&oe=6712D71C", 
        "age": 20, 
        "student_id": "65010814"
    },
    {
        "name": "รฐิตา สว่างเดือน", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 20, 
        "student_id": "65010905"
    },
    {
        "name": "รมย์ชลี แก้วสา", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 20, 
        "student_id": "65010911"
    },
    {
        "name": "วสันต์ บุญสงค์", 
        "image": "https://www.iote.kmitl.ac.th/wp-content/uploads/2024/09/67630-240x300.jpg", 
        "age": 20, 
        "student_id": "65010970"
    },
    {
        "name": "อุษมา พีธรากร", 
        "image": "https://cdn.britannica.com/74/252374-050-AD45E98E/dog-breed-height-comparison.jpg", 
        "age": 20, 
        "student_id": "65011236"
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
