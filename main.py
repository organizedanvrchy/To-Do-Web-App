import streamlit as st
import functions

todos = functions.get_tasks()

def add_todo():
  todo = st.session_state["new_todo"]
  todos.append(todo)
  if todo:
    functions.add_tasks(todos)


st.title("To-Do App")
st.subheader("Welcome.")
st.write("This App increases your productivity.")


for todo in todos:
  st.checkbox(todo)

st.text_input(label="Enter a To-Do", 
              label_visibility="hidden", 
              placeholder="Enter a To-Do",
              on_change=add_todo, key="new_todo")

  