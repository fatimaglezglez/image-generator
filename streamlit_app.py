import replicate
import streamlit as st

# UI configurations
st.set_page_config(page_title="Simple Image Generator", page_icon=":sparkles:", layout="wide")

# API Tokens and endpoints from `.streamlit/secrets.toml` file
REPLICATE_API_TOKEN = st.secrets["r8_GvKzzWD9basAu2cu0Y8qqDGzLM8HivZ0HKqAN"]
REPLICATE_MODEL_ENDPOINTSTABILITY = st.secrets["stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"]

def generate_image(prompt: str):
    """
    Generate an image based on a given prompt.

    Args:
        prompt (str): Text prompt for the image generation.

    Returns:
        Image or error message.
    """
    try:
        output = replicate.predictions.create(
            version=REPLICATE_MODEL_ENDPOINT,
            input=prompt,
            api_token=REPLICATE_API_TOKEN
        )

        if output:
            return output[0]["output"]
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to run the Streamlit application.

    This function displays a simple form for user input and calls the
    generate_image function to display the resulting image.
    """
    st.title("Simple Image Generator")
    
    with st.form("image_gen_form"):
        prompt = st.text_area("Enter your prompt here", "A futuristic cityscape at sunset")
        submitted = st.form_submit_button("Generate Image")
    
    if submitted and prompt:
        with st.spinner('Generating your image...'):
            result = generate_image(prompt)
            if result and not result.startswith("An error occurred"):
                st.image(result, caption="Generated Image")
            else:
                st.error(result)

if __name__ == "__main__":
    main()

