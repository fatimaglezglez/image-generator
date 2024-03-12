import replicate
import streamlit as st

# Simplified app for generating images with Replicate

# UI configuration
st.set_page_config(page_title="Simple Replicate Image Generator",
                   page_icon=":art:",
                   layout="centered")

# Display a header
st.markdown("# Simple Image Generator")

# API Token and model endpoint from `.streamlit/secrets.toml` file
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
REPLICATE_MODEL_ENDPOINT = st.secrets["REPLICATE_MODEL_ENDPOINT"]

# Setup Replicate
replicate.api_token = REPLICATE_API_TOKEN

# Input prompt
prompt = st.text_input("Enter your prompt:", value="A beautiful landscape")

# Submit button
if st.button('Generate Image'):
    with st.spinner('Generating image...'):
        try:
            output = replicate.run(REPLICATE_MODEL_ENDPOINT, inputs={"prompt": prompt})

            if output:
                st.image(output[0], caption="Generated Image")
            else:
                st.error("No output from the model")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Note: This is a simplified version and assumes that the REPLICATE_MODEL_ENDPOINT
# is correctly configured to accept a prompt and generate an image.
