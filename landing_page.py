import streamlit as st

contact = st.Page(page="pages/contact.py", title="Contact", icon="📞")
about = st.Page(page="pages/about.py", title="About", icon="ℹ️")
home= st.Page(page="pages/home.py", title="Home", icon="🏠")

pg = st.navigation({
    'Home' : [home],
   "all_contact_about" :[contact, about]}
)   

pg.run()

