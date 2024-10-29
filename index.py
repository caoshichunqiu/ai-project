import streamlit as st


st.title("AI大模型")

col,col1,col2= st.columns(3)
with col:
    st.image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1mluxx.img?w=534&h=356&m=6",use_column_width=True)
    flag = st.button("基础", use_container_width=True)
    if flag:
        st.switch_page("pages/demo1.py")
    # flag=st.button("基础版")
    # if flag:
    #     st.switch_page("pages/demo.py")

with col1:
    st.image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1mluxx.img?w=534&h=356&m=6",use_column_width=True)
    flag=st.button("逆子", use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")

    # flag=st.button("逆子版")
    # if flag:
    #     st.switch_page("pages/demo1.py")

with col2:
    st.image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1mluxx.img?w=534&h=356&m=6",use_column_width=True)
    flag=st.button("文生图", use_container_width=True)
    if flag:
        st.switch_page("pages/textpaint.py")