import streamlit as st
from PIL import Image as ig


def grey_photos(photo):
    if photo:
        # Create a pillow image instant
        image = ig.open(photo)
        # convert the image grey scale
        gre_image = image.convert("L")
        # Show the image
        st.image(gre_image)
