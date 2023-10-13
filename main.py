#이게 하드 코딩

import streamlit as st
import langchain_helper

st.title("Restraurant name generator")

cuisine = st.sidebar.selectbox("PICK a cuisine.", ("KOREAN","INDIAN","MEXICAN","ITALIAN","AMERICAN"))


if cuisine:
    #항목 선택으로 얻은 결과를 *응답을* 다음 응답에서 사용
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    #쉼표로 구분된 문자열이 있을 때마다 분할함수 호출하기~ spilit
    st.write("**Menu_Items**")
    for item in menu_items:
        st.write("-", item)








