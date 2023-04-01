import streamlit as st
import functions as fc

# Starting the App
st.header("Camera app")
# Taking a Picture

# with st.expander(label="") The lines below will be indented
with st.expander("Take a picture"):
    photo = st.camera_input("")

uploaded_image = st.file_uploader("Upload Image")

fc.grey_photos(photo)
fc.grey_photos(uploaded_image)
