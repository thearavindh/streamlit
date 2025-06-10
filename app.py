import streamlit as st
from replicate_backend import generate_video

st.set_page_config(page_title="AI Product Ad Generator", layout="centered")
st.title("🛍️ AI Product Ad Video Generator")
st.markdown("Enter a product description and get a short AI-generated promo video!")

prompt = st.text_area("📝 Product Description", placeholder="e.g. A spinning perfume bottle on black background with spotlight")

if st.button("🎥 Generate Video"):
    if prompt.strip() == "":
        st.warning("Please enter a product description.")
    else:
        with st.spinner("Generating video... please wait (30–60 seconds)"):
            video_url = generate_video(prompt)
            if video_url:
                st.video(video_url)
                st.success("Video generated!")
            else:
                st.error("Something went wrong. Please try again.")
