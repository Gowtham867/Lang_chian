import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from PIL import Image
import io
import base64

llm = ChatOllama(model="llava", temperature=0)
st.title("Simple Landmark Helper")
uploaded_img = st.file_uploader(
    "Upload a landmark image",
    type=["jpg", "jpeg", "png"]
)
img_b64 = None  
if uploaded_img:
    st.image(uploaded_img, caption="Uploaded image", use_container_width=True)

    img = Image.open(uploaded_img).convert("RGB")
    img = img.resize((512, 512))
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

qn = st.text_input("Enter your question about the landmark")

if qn:
    if not uploaded_img or not img_b64:
        st.warning("Please upload an image first")
    else:
        message = HumanMessage(
            content=[
                {"type": "text", "text": qn},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{img_b64}"}
            ]
        )
        
        with st.spinner("Processing your request..."):
            response = llm.invoke([message])
        
        st.write(response.content)
