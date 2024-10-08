import re
import streamlit as st
import pandas as pd
import joblib
# โหลดโมเดล Random Forest
# model = joblib.load('random_forest_model.pkl')
    # ทำการทำนายว่ามี Portscan หรือไม่
def parse_tcp_info(info):
    # พาร์ส Source Port, Destination Port, และ Flags เช่น SYN, ACK, RST
    match = re.match(r'(\d+)\s+>\s+(\d+)\s+\[([A-Z, ]+)\]', info)
    if match:
        src_port = match.group(1)
        dest_port = match.group(2)
        flags = match.group(3)
        return src_port, dest_port, flags
    return None, None, None

# ฟังก์ชันสำหรับทำนายการโจมตี
# def predict_attack(data):
#     predictions = model.predict(data)
#     return predictions

# Streamlit UI
st.title("CSV File Portscan Detection")

# อัปโหลดไฟล์ CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # อ่านข้อมูลจากไฟล์ CSV
    df = pd.read_csv(uploaded_file)
    
    # แสดงข้อมูลที่อัปโหลด
    st.write("Uploaded CSV Data:", df)

    # เลือกเฉพาะฟีเจอร์ที่จำเป็นสำหรับโมเดล
    #data_for_prediction = df[features].fillna(0)  # จัดการ missing value

    df['Source Port'], df['Destination Port'], df['TCP Flags'] = zip(*df['Info'].apply(parse_tcp_info))
    df = df.dropna()
    # เพิ่มฟีเจอร์การนับแพ็กเก็ตและเวลา
    df['Total Fwd Packets'] = (df['Protocol'] == 'TCP').astype(int)  # สำหรับ TCP เท่านั้น
    df['Total Backward Packets'] = (df['Protocol'] == 'ICMP').astype(int)  # สำหรับ ICMP เท่านั้น
    df['Flow Duration'] = df['Time'].diff().fillna(0)  # ความแตกต่างระหว่าง Timestamp

    # ฟีเจอร์ที่เกี่ยวกับ FLAG
    df['SYN Flag Count'] = df['TCP Flags'].apply(lambda x: x.count('SYN'))
    df['FIN Flag Count'] = df['TCP Flags'].apply(lambda x: x.count('FIN'))
    df['ACK Flag Count'] = df['TCP Flags'].apply(lambda x: x.count('ACK'))

    # คำนวณ Flow Packets/s และ Average Packet Size
    df['Flow Packets/s'] = df['Total Fwd Packets'] / (df['Flow Duration'] + 1e-9)  # หลีกเลี่ยงการหารด้วย 0


    # คำนวณ Idle Mean และ Idle Std (สมมติว่า Idle คือระยะเวลาที่ไม่มีการเชื่อมต่อ)
    df['Idle Mean'] = df['Flow Duration'].mean()
    df['Idle Std'] = df['Flow Duration'].std()

    # คำนวณ Fwd to Bwd Ratio
    df['Fwd to Bwd Ratio'] = df['Total Fwd Packets'] / (df['Total Backward Packets'] + 1e-9)

    # คำนวณ Connection Rate
    df['Connection Rate'] = df['Total Fwd Packets'] / (df['Flow Duration'] + 1e-9)

    # คำนวณ Time between Connections
    df['Time between Connections'] = df['Time'].diff().fillna(0)

    # คำนวณ Scan Count และ Unique Dest Port Count
    df['IP Scan Count'] = df.groupby('Source')['Source'].transform('count')
    df['Unique Dest Port Count'] = df.groupby('Source')['Destination Port'].transform('nunique')
    df.to_csv("pcapp.csv")
    st.write(df)