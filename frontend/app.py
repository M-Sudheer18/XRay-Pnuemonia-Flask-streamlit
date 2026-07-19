# Chest X-Ray Pneumonia Detection
# Streamlit Frontend

# from api import *
import streamlit as st
from PIL import Image
from api import check_status, predict_image


# Page Configuration
st.set_page_config(
    page_title="Chest X-Ray Pneumonia Detection",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# Title
st.subheader("🩻 Chest X-Ray Pneumonia Detection")
st.markdown(
    "Upload a chest X-ray image and choose a deep learning model for prediction."
)
st.divider()


# Sidebar
with st.sidebar:
    st.sidebar.subheader("🩻 X-Ray Classifier")
    st.markdown("---")
    st.subheader('🤖 Select Model')

    # Model Selection
    MODEL_OPTIONS = {
        "🧠 CNN (10 Epochs)": "cnn10",
        "⚡ CNN (20 Epochs)": "cnn20",
        "⭐ VGG16 Transfer Learning": "vgg16"
    }

    selected = st.radio(
        "",
        list(MODEL_OPTIONS.keys()),
        label_visibility="collapsed"
    )

    model = MODEL_OPTIONS[selected]
    
    model_info = {
            "cnn10": {
                "name": "CNN (10 Epochs)",
                "acc": "95.2%",
                "desc": "Basic CNN trained for 10 epochs."
            },
            "cnn20": {
                "name": "CNN (20 Epochs)",
                "acc": "97.1%",
                "desc": "Improved CNN trained for 20 epochs."
            },
            "vgg16": {
                "name": "VGG16 Transfer Learning",
                "acc": "98.5%",
                "desc": "Pretrained VGG16 with transfer learning."
        }
    }

    st.success(f"**{model_info[model]['name']}**")
    st.markdown("**Accuracy**")
    st.markdown(f"### {model_info[model]['acc']}")

    st.caption(model_info[model]['desc'])
    st.markdown('---')

    st.write("📄 Prediction Classes")

    st.success("🟢 NORMAL")
    st.error("🔴 PNEUMONIA")
    
    st.markdown("---")
    
    st.subheader("📂 Supported Formats")
    st.write("✔ JPG")
    st.write("✔ JPEG")
    st.write("✔ PNG")

    st.markdown("---")

    st.subheader("ℹ Project")

    st.write("🧠 Models : 3")
    st.write("🩻 Classes : 2")
    st.write("📐 Image Size : 100 × 100")
    st.write("⚙ Backend : Flask")
    st.write("🤖 Framework : TensorFlow")
    
    st.markdown("---")
    st.subheader("👨‍💻 Developer")

    st.caption("""
    **Sudheer Muthyala**

    B.Tech (ECE) | AI Engineer

    Built with ❤️ using Flask, TensorFlow & Streamlit.
    """)


# Image Upload
st.write("📤 Upload Chest X-Ray Image")

left, center, right = st.columns([2, 3, 2])

with center:

    uploaded_file = st.file_uploader(
        "",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.subheader("🩻 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

        if st.button(
            "🔍 Predict",
            use_container_width=True
        ):
            uploaded_file.seek(0)

            with st.spinner("Analyzing X-Ray..."):
                result = predict_image(
                    uploaded_file,
                    model
                )

            prediction = result["prediction"]
            confidence = result["confidence"]

            st.markdown("---")

            if prediction == "NORMAL":
                st.success(f"🟢 {prediction}")
            else:
                st.error(f"🔴 {prediction}")

            st.markdown("**Confidence**")
            st.markdown(f"### {confidence:.2f}%")

            st.progress(confidence / 100)

            st.markdown("**Class Probabilities**")

            st.write("🟢 NORMAL")
            st.progress(result["probabilities"]["NORMAL"] / 100)

            st.write("🔴 PNEUMONIA")
            st.progress(result["probabilities"]["PNEUMONIA"] / 100)

            st.info(f"🤖 Model: {result['model']}")