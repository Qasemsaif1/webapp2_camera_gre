import streamlit as st
from PIL import Image as ig

# Starting the App
st.header("Camera app")

# Taking a Picture

# with st.expander(label="") Thelines bilow will be indented
button = st.button ("Open Camera")
if button:
    photo = st.camera_input("")

    if photo:
        # Create a pillow image instant
        image = ig.open (photo)
        # convert the image grey scale
        gre_image = image.convert("L")
        # Show the image
        st.image(gre_image)






