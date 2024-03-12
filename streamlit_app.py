import replicate
import streamlit as st

# Simplified app for generating images with Replicate

# UI configuration
st.set_page_config(page_title="Fatima's App",
                   page_icon=":heart:",
                   layout="centered")

# Display a header
st.markdown("# simple image generator :)")

# API Token and model 

REPLICATE_MODEL_ENDPOINTSTABILITY = "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
#REPLICATE_MODEL_ENDPOINTSTABILITY = "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2"

# Input prompt
prompt = st.text_input("enter your prompt:", value="vase with flowers")
style = st.selectbox(
    'pick a style:',
    ('art-nouveau illustration', 'abstract art', 'stained glass', 'photo')
)
prompt_with_style = f"{style} {prompt}"
# Submit button
if st.button('generate image'):
    with st.spinner('generating image...'):
        try:
            # Running the model with specific parameters
            output = replicate.run(
                            REPLICATE_MODEL_ENDPOINTSTABILITY,
                            input={
                                "prompt": prompt_with_style,
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
                st.image(output[0], caption="generated image")
            else:
                st.error("No output from the model")
        except Exception as e:
            st.error(f"An error occurred: {e}")
