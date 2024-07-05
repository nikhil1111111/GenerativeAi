import streamlit as st
from PIL import Image
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from poem_generator import generate_poem, generate_image

prompt_template = PromptTemplate(
    template="Write a {style} poem about {topic} with a {rhyme_scheme} rhyme scheme",
    variables=["style", "topic", "rhyme_scheme"]
)

llm_chain = LLMChain(prompt=prompt_template, llm=generate_poem)

st.title("Advanced Poem Writer")
st.write("This app generates poems and images using advanced language and image models.")

topic = st.text_input("Enter a topic for the poem:")
style = st.selectbox("Select the style of the poem:", ["haiku", "sonnet", "free verse"])
rhyme_scheme = st.selectbox("Select the rhyme scheme:", ["ABAB", "AABB", "none"])
max_length = st.slider("Select the maximum length of the poem:", 50, 500, 100)

if st.button("Generate Poem"):
    with st.spinner("Generating..."):
        prompt = prompt_template(style=style, topic=topic, rhyme_scheme=rhyme_scheme)
        poem = generate_poem(prompt, max_length)
        st.write(poem)
        image_prompt = f"An artistic representation of the following poem: {poem}"
        negative_prompt = ""
        num_inference_steps = 28
        guidance_scale = 7.0
        image = generate_image(image_prompt, negative_prompt, num_inference_steps, guidance_scale)
        st.image(image, caption="Generated Image")








