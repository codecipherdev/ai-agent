import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# OpenAI setup
import os
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

st.title("My Free AI Agent 🤖")

prompt = st.text_area("Enter your task or question:")

if st.button("Run AI Agent"):
    if prompt:
        llm = OpenAI(temperature=0.7)
        template = PromptTemplate(input_variables=["task"], template="You are my AI agent. Do this: {task}")
        chain = LLMChain(llm=llm, prompt=template)
        output = chain.run(task=prompt)
        st.write("### Result:")
        st.write(output)
    else:
        st.warning("Please enter a task.")
