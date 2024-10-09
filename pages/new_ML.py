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
def predict_attack(data):
    predictions = model.predict(data)
    return predictions
st.title("CSV File Portscan Detection")

# อัปโหลดไฟล์ CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # อ่านข้อมูลจากไฟล์ CSV
    df = pd.read_csv(uploaded_file)
    
    # แสดงข้อมูลที่อัปโหลด
    st.write("Uploaded CSV Data:", df)
    df = df.drop(columns='Unnamed: 0')
    # โหลดโมเดล Random Forest
    model = joblib.load('random_forest_model.pkl')
    predictions = predict_attack(df)
    df['Portscan Prediction'] = predictions
    # ไฮไลท์คอลัมน์ที่เป็น Portscan
    def highlight_portscan(row):
        return ['background-color: red' if row['Portscan Prediction'] == 1 else '' for _ in row]
    # แสดงผล DataFrame พร้อมการไฮไลท์
    st.dataframe(df.style.apply(highlight_portscan, axis=1))
