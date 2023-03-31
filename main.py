import streamlit as st
from PIL import Image as ig


# Starting the App
st.header("Camera app")

# Taking a Picture

# with st.expander(label="") Thelines bilow will be indented
with st.expander("Take a picture"):
    photo = st.camera_input("")

uploaded_image = st.file_uploader("Upload Image")

if photo:
    # Create a pillow image instant
    image = ig.open (photo)
    # convert the image grey scale
    gre_image = image.convert("L")
    # Show the image
    st.image(gre_image)


if uploaded_image:
    # Create a pillow image instant
    image = ig.open (uploaded_image)
    # convert the image grey scale
    gre_image = uploaded_image.convert("L")
    # Show the image
    st.image(gre_image)




