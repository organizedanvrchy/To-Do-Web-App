import streamlit as st
import functions

<<<<<<< HEAD
=======
# Load existing to-dos
>>>>>>> d846a0c (Update to main.py. Fixed erroneous duplication of last to-do upon checking the box for completion. Fixed input text box not clearing current text. Added requirements.txt file.)
todos = functions.get_tasks()

def add_todo():
  todo = st.session_state["new_todo"]
<<<<<<< HEAD
  todos.append(todo)
  if todo:
    functions.add_tasks(todos)


st.title("To-Do App")
st.subheader("Welcome.")
st.write("This App increases your productivity.")

for i, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todos.pop(i)
    functions.add_tasks(todos)
    del st.session_state[todo]
    st.rerun()

st.text_input(label="Enter a To-Do", 
              label_visibility="hidden", 
              placeholder="Enter a To-Do",
              on_change=add_todo, key="new_todo")
=======
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
>>>>>>> d846a0c (Update to main.py. Fixed erroneous duplication of last to-do upon checking the box for completion. Fixed input text box not clearing current text. Added requirements.txt file.)

  