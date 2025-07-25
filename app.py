import streamlit as st
from transformers import pipeline
import sqlite3

st.title("🧑‍💻 My Free AI Agent (Hugging Face, Lightweight)")

prompt = st.text_area("What task do you want me to do?")

if st.button("Run Agent"):
    if prompt:
        generator = pipeline('text-generation', model='distilgpt2')

        # ✅ Add instruction to guide the model
        input_text = f"Write a short poem:\n{prompt}"

        result = generator(
            input_text,
            max_new_tokens=50,
            truncation=True
        )
        output = result[0]['generated_text']

        st.write("### ✅ Result")
        st.write(output)

        conn = sqlite3.connect("logs.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS logs (prompt TEXT, output TEXT)''')
        c.execute("INSERT INTO logs VALUES (?, ?)", (prompt, output))
        conn.commit()
        conn.close()

    else:
        st.warning("Please enter a task.")
