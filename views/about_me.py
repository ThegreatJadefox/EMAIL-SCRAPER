import streamlit as st
from support.support import support_me


@st.dialog("Support Me")
def  show_contact_form():
    support_me()


# Hero section
col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")
with col1:
    st.image("static/1.jpg", width = 230)
with col2:
    st.title("Akintola Oladapo", anchor=False)
    st.write(
        "Intermediate Python Programmer from Nigeria, Currently self-learning python programming in hopes of one day becoming a mega business owner in the field."
    )

    if st.button("🤝Support Me"):
        show_contact_form()

#SKILLS
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
-Programming: Python(Tkinter, Numpy, Streamlit, HTML(Basic))\n
-Database: SQLlite 3(Basic)
"""
)

