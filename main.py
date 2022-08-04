import streamlit as st
view = [300, 200, 100, 500]
show_raw = st.checkbox('show raw data')
if show_raw==True:
    st.write('# raw data')
    view
st.write('# table') #표로보기
st.table(view)
st.write('# bar graph') #그래프로보기
st.bar_chart(view)