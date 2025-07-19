import streamlit as st
from transformers import pipeline
import sqlite3

st.title("🧑‍💻 My Free AI Agent (Hugging Face)")

# Text input
prompt = st.text_area("What task do you want me to do?")

# When user clicks button
if st.button("Run Agent"):
    if prompt:
        # Load a text-generation pipeline using Falcon-7B-Instruct
        generator = pipeline('text-generation', model='tiiuae/falcon-7b-instruct')

        # Generate output with truncation fix
        result = generator(
            prompt,
            max_length=200,
            truncation=True   # ✅ avoids warning
        )
        output = result[0]['generated_text']

        # Show result in the app
        st.write("### ✅ Result")
        st.write(output)

        # Save prompt + output to SQLite
        conn = sqlite3.connect("logs.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS logs (prompt TEXT, output TEXT)''')
        c.execute("INSERT INTO logs VALUES (?, ?)", (prompt, output))
        conn.commit()
        conn.close()

    else:
        st.warning("Please enter a task.")
