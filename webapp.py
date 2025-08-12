import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



st.set_page_config(page_title="MST Skin color Analysis",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

st.title("MST Skin Color Analysis")
st.markdown("---")
left_column, right_column = st.columns([1, 2])  # Left column 1/3, right column 2/3

with left_column:
    st.header("Upload Image file")
    image=st.file_uploader("Upload your image to analyse",type=['jpg','png','jpeg'])
    if image is not None:
        img=Image.open(image)
        img_array=np.array(img)
    else:
        st.info(" Upload an image to get started")

with right_column:
    st.write("MST scale offers a more holistic view that can be applied across diverse demographics, providing insights into skin sensitivity and adaptability")
    st.image('MST_SKIN_TONE_SCALE.png', caption="Monk skin tone(MST) scale")
    if image is not None:
        fig, ax = plt.subplots(figsize=(8, 4))
        colors = ('red', 'green', 'blue')
        for i, color in enumerate(colors):
            ax.hist(img_array[:, :, i].ravel(), bins=256, color=color, alpha=0.6, label=f'{color} channel')
        ax.set_xlabel('Pixel Intensity')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.set_title('RGB Color Distribution')
        st.pyplot(fig)
    else:
        st.info("Add image to upload box")

