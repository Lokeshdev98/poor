import streamlit as st
import os
from datetime import datetime

# Set upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Streamlit UI
st.set_page_config(page_title="Helping for Poor", layout="centered")
st.title("🙏 Please Help the Poor")
st.subheader("Submit Payment Details")

# Form for donation
with st.form(key='donation_form'):
    name = st.text_input("Enter Your Name")
    email = st.text_input("Enter Your Email")
    uploaded_file = st.file_uploader("Upload Payment File", type=['pdf', 'doc', 'docx'])
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if name and email and uploaded_file:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Insert into MySQL database
            query = "INSERT INTO donations (name, email, payment_file, created_at) VALUES (%s, %s, %s, %s)"
            values = (name, email, uploaded_file.name, datetime.now())
            cursor.execute(query, values)

            st.success("🎉 Submission Successful!")
        else:
            st.error("⚠️ Please fill all the fields and upload a file.")

# Contact Information
st.markdown("""
### 📞 pay on
- Phone: 9110585108@ybl  
""")
st.markdown("""
### 📞 Contact Us
- Phone: 6281770026  
- Email: lokeshdevarakonda143@gmail.com
""")
