import pie_chart as pieC
import stack_chart as stackC
import bar_chart as barC
import line_chart as lineC
import streamlit as st
st.set_page_config(layout="wide")
st.title("The impact of covid-19 vaccination campaigns in malaysia",)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.text(" ")
st.text(" ")
col1, col2 = st.columns(2)

dashboard = st.radio("Choose dashboard",("Dashboard 1","Dashboard 2","Dashboard 3"))

if dashboard == "Dashboard 1":
    col1.pyplot(barC.plot_bar())
    col2.pyplot(lineC.plot_line())

if dashboard == "Dashboard 2":
    col1.text("Under construction")
    col2.text("Under construction")

if dashboard == "Dashboard 3":
    col1.pyplot(pieC.plot_pie())
    col2.pyplot(stackC.plot_stack())