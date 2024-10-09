import streamlit as st
import pandas as pd
import numpy as np
import gdown
import plotly.graph_objects as go

st.set_page_config(
    page_title="Log Monitoring",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache(allow_output_mutation=True)
def load_data():
    # URL ของไฟล์ CSV บน Google Drive
    # file_url = 'https://drive.google.com/uc?id=1iFAo1LPUijiDHR3dMWnhcDQRNJLSLpLj'

    # # ดาวน์โหลดไฟล์ CSV จาก Google Drive
    # gdown.download(file_url, 'data.parquet', quiet=False)

    # โหลดข้อมูลจากไฟล์ CSV
    combined_df  = pd.read_parquet('/mount/src/ai_security_app/pages/Out_test.parquet')
    #combined_df = pd.read_parquet("parquet_dir_access/combined.parquet")
    return combined_df

@st.cache
def preprocess_data(combined_df):
    combined_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    combined_df.dropna(inplace=True)
    combined_df.columns = combined_df.columns.str.strip().str.replace(' ', '_')
    combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'])
    combined_df = combined_df.set_index('Timestamp')
    combined_df = combined_df.resample('5S').agg({
        'Source_IP': 'first',
        'Source_Port': 'first',
        'Destination_IP': 'first',
        'Destination_Port': 'first',
        'Flow_Bytes/s': 'sum',
        'Total_Fwd_Packets': 'sum',
        'Total_Backward_Packets': 'sum',
        'Label': 'first',
        'Protocol': 'first'
    }).reset_index()
    return combined_df

combined_df = load_data()
combined_df = preprocess_data(combined_df)

# Sidebar Content
st.sidebar.title("Select Feature to Display")
def pie_chart_protocol():
    st.markdown("<h3 style='color: #00FF00;'>🛡️ Pie Chart of Protocols</h3>", unsafe_allow_html=True)
    protocol_counts = combined_df['Protocol'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=['TCP', 'UDP', 'ICMP'],
                                 textfont=dict(size=18, color='white', family="Arial"),
                                  values=protocol_counts.values, marker=dict(colors=['#FF0000', '#00FF00', '#FFFF00']))])
    fig.update_layout(
        legend=dict(
        font=dict(size=16)  # Adjust this value to increase/decrease legend font size
    )
    )
    st.plotly_chart(fig, use_container_width=True)

def show_flow_bytes():
    st.sidebar.header("Flow Bytes Analysis")

    st.markdown("<h3 style='color: #00FF00;'>📊 Flow Bytes Over Time</h3>", unsafe_allow_html=True)
    selected_feature = st.sidebar.selectbox('Select Feature to Display:', ['Flow_Bytes/s', 'Total_Fwd_Packets', 'Total_Backward_Packets'])
    fig = go.Figure()
    
    for label in combined_df['Label'].unique():
        ddos = combined_df[combined_df['Label'] == label]
        fig.add_trace(go.Scatter(x=ddos['Timestamp'], y=ddos[selected_feature], mode='lines', name=label, line=dict(width=2)))

    fig.update_layout(title=f'{selected_feature} During DDoS Attacks', xaxis_title='Timestamp', yaxis_title=selected_feature, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
def match():
    st.sidebar.header("Feature Comparison")
    st.markdown("<h3 style='color: #00FF00;'>⚖️ Feature Comparison</h3>", unsafe_allow_html=True)

    # ปุ่มเลือก 2D หรือ 3D
    plot_type = st.radio("Select Plot Type", ["2D", "3D"])

    # เลือกฟีเจอร์สำหรับแกน X และ Y
    x_feature = st.sidebar.selectbox('Select X-axis Feature:', combined_df.columns)
    y_feature = st.sidebar.selectbox('Select Y-axis Feature:', combined_df.columns)

    # หากผู้ใช้เลือก 3D ให้มีการเลือกฟีเจอร์สำหรับแกน Z
    if plot_type == "3D":
        z_feature = st.sidebar.selectbox('Select Z-axis Feature:', combined_df.columns)

    fig = go.Figure()

    # แสดงผลแบบ 2D
    if plot_type == "2D":
        for label in combined_df['Label'].unique():
            ddos = combined_df[combined_df['Label'] == label]
            fig.add_trace(go.Scatter(
                x=ddos[x_feature], 
                y=ddos[y_feature], 
                mode='markers',
                name=label,
                marker=dict(size=5)
            ))

        fig.update_layout(
            title=f'{y_feature} vs {x_feature} During DDoS Attacks',
            xaxis_title=x_feature,
            yaxis_title=y_feature,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )

    # แสดงผลแบบ 3D
    elif plot_type == "3D":
        for label in combined_df['Label'].unique():
            ddos = combined_df[combined_df['Label'] == label]
            fig.add_trace(go.Scatter3d(
                x=ddos[x_feature], 
                y=ddos[y_feature], 
                z=ddos[z_feature], 
                mode='markers',
                name=label,
                marker=dict(size=5)
            ))

        fig.update_layout(
            title=f'{z_feature} vs {y_feature} vs {x_feature} During DDoS Attacks',
            scene=dict(
                xaxis_title=x_feature,
                yaxis_title=y_feature,
                zaxis_title=z_feature
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )

    # แสดงกราฟ
    st.plotly_chart(fig, use_container_width=True)
def violin_plot():
    st.sidebar.header("Violin Analysis")
    st.markdown("<h3 style='color: #00FF00;'>🎻 Violin Plot of Attack Types</h3>", unsafe_allow_html=True)
    selected_feature = st.sidebar.selectbox('Select Feature for Violin Plot:', ['Flow_Bytes/s', 'Total_Fwd_Packets', 'Total_Backward_Packets'])
    colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#4B0082', '#9400D3']
    fig = go.Figure()
    
    unique_labels = combined_df['Label'].unique()
    for idx, label in enumerate(unique_labels):
        ddos = combined_df[combined_df['Label'] == label]
        fig.add_trace(go.Violin(
            y=ddos[selected_feature],
            name=label,
            box_visible=True,
            line_color=colors[idx % len(colors)],
            opacity=0.6
        ))

    fig.update_layout(
        title=f'Violin Plot of {selected_feature} by Attack Type',
        yaxis_title=selected_feature,
        xaxis_title='Attack Type',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig, use_container_width=True)

# เรียกใช้ฟังก์ชันต่าง ๆ
pie_chart_protocol()
show_flow_bytes()
match()
violin_plot()

# ตั้งค่าธีม
st.markdown("""
<style>
    .reportview-container {
        background: #1E1E1E;
        color: white;
    }
    .sidebar .sidebar-content {
        background: #2E2E2E;
    }
    h3 {
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)
