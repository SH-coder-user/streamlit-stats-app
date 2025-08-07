import streamlit as st
import matplotlib.pyplot as plt
from app.analysis import generate_data, analyze_data

st.title("📊 난수 기반 통계 분석기")

n = st.slider("데이터 갯수", 100, 5000, 1000)
mean = st.number_input("평균", value=0.0)
std = st.number_input("표준편차", value=1.0)

if st.button("데이터 생성 및 분석"):
    data = generate_data(n=n, mean=mean, std=std)
    stats = analyze_data(data)

    st.subheader("📈 통계 요약")
    st.write(stats)

    st.subheader("📉 히스토그램")
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, edgecolor='black')
    ax.set_title("히스토그램")
    st.pyplot(fig)

