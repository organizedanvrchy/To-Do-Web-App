import streamlit as st
import functions

# Load existing to-dos
todos = functions.get_tasks()

def add_todo():
  todo = st.session_state["new_todo"]
  # Only add if input is not empty
  if todo:
    todos.append(todo)
    functions.add_tasks(todos)

    # Clear input box
    st.session_state["new_todo"] = ""

st.title("To-Do App")
st.subheader("Welcome.")
st.write("Use this App to increases your productivity.")

# Display list of to-dos with checkboxes
for i, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    # Remove completed to-do
    todos.pop(i)

    # Update file
    functions.add_tasks(todos)

    # Re-run app to refresh list
    # del st.session_state[todo]
    st.rerun()

# Input box for adding new to-dos
st.text_input(label="Enter a To-Do", 
              label_visibility="hidden", 
              placeholder="Enter a To-Do",
              on_change=add_todo, 
              key="new_todo",
              value=st.session_state.get("new_todo", ""))
