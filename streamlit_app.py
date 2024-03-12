import replicate
import streamlit as st

# Simplified app for generating images with Replicate

# UI configuration
st.set_page_config(page_title="Fatima's App",
                   page_icon=":heart:",
                   layout="centered")

# Display a header
st.markdown("# Simple Image Generator :))")

# API Token and model endpoint from `.streamlit/secrets.toml` file
REPLICATE_API_TOKEN = "r8_ehJx4zMgPENagZGnfeFnZmx6fSfpBjM0teoQf"
REPLICATE_MODEL_ENDPOINTSTABILITY = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"

# Setup Replicate
replicate.api_token = REPLICATE_API_TOKEN

# Input prompt

# Input prompt
prompt = st.text_input("Enter your prompt:", value="A beautiful landscape")

# Submit button
if st.button('Generate Image'):
    with st.spinner('Generating image...'):
        try:
            # Running the model with specific parameters
        output = replicate.run(
                            REPLICATE_MODEL_ENDPOINTSTABILITY,
                            input={
                                "prompt": prompt,
                                "width": 768,
                                "height": 768,
                                "num_outputs": 1,
                                "scheduler": "K_EULER",
                                "num_inference_steps": 25,
                                "guidance_scale": 7.5,
                                "prompt_stregth":  0.8,
                                "refine": "expert_ensemble_refiner",
                                "high_noise_frac":  0.8
                            }
            )
          if output:
                # Assuming `output` is a URL to the generated image
                st.image(output[0], caption="Generated Image")
          else:
                st.error("No output from the model")
        except Exception as e:
            st.error(f"An error occurred: {e}")
