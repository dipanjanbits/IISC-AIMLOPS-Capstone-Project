import streamlit as st
import math

st.title("AI - Plant Disease Detection and Farmer Assistance")

show_images = st.checkbox("Show uploaded images", value=True)

uploaded_images = st.file_uploader("Upload an image", 
                                   type=['png', 'jpg', 'jpeg'], 
                                   accept_multiple_files=True
                                   )

if uploaded_images is not None and show_images:

    cols_per_row = 4
    num_images = len(uploaded_images)
    num_rows = math.ceil(num_images / cols_per_row)

    # for image in uploaded_images:
    #     # bytes_data = image.read()
    #     st.write("filename: ", image.name)
    #     # st.write(bytes_data)
    #     st.markdown(
    #         """
    #         <div style="border: 2px solid #4CAF50; border-radius: 2px; 
    #                     background-color: brown; text-align: center;">
    #             <strong>Image uploaded!</strong>
    #         </div>
    #         """, unsafe_allow_html=True)
    #     st.image(uploaded_images, caption="Uploaded Image")

    st.markdown(
    f"""
    <div style="border: 1px solid #E2B007; border-radius: 1px;">
    </div>
    """, unsafe_allow_html=True)
    for row_idx in range(num_rows):
        cols = st.columns(cols_per_row)
        for col_idx in range(cols_per_row):
            idx = row_idx * cols_per_row + col_idx
            if idx < num_images:
                image = uploaded_images[idx]
                bytes_data = image.read()

                with cols[col_idx]:
                    st.image(
                        bytes_data,   #uploaded_images,
                        caption=image.name
                        )