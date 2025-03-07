import streamlit as st
import functions

todos = functions.get_tasks()
st.title("To-Do App")
st.subheader("Welcome.")
st.write("This App increases your productivity.")


for todo in todos:
  st.checkbox(todo)

user_input = st.text_input(label="Enter a To-Do", label_visibility="hidden", placeholder="Enter a To-Do")
if user_input:
  functions.add_tasks(user_input)
  