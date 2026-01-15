import streamlit as st
import pandas as pd

st.title("Оценки и ученици")

if "uchenici" not in st.session_state:
    st.session_state.uchenici = {
        "Alex": 0,
        "NIki": 0,
        "Viktor": 0,
        "Dimitar": 0
    }

if "grades" not in st.session_state:
    st.session_state.grades = {
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

st.subheader("Избери ученици и оценките им")

color = st.selectbox("ученик:", list(st.session_state.uchenici.keys()))
sport = st.selectbox("оценка:", list(st.session_state.grades.keys()))


if st.button("Запази избора"):
    st.session_state.uchenici[color] += 1
    st.session_state.grades[sport] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("☑️ Резултати")

st.write("ученик")
colors_df = pd.DataFrame.from_dict(
    st.session_state.uchenici, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

st.write("оценки")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)
