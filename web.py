import streamlit as st
import functions
import time

#https://azulafire-todo-web-web-thk8d9.streamlit.app/

# WEB Functions

todos = functions.gui_get_todos()

def get_count():
  count = len(functions.gui_get_todos())
  return f"Current To-Do Count: {count}"

def get_date():
  now = time.strftime("%b %d, %Y %H:%M:%S")
  return now

def add_todo():
  new_todo = st.session_state["-ADD-"]
  todos.append(new_todo.title() + "\n")
  functions.gui_write_todos(todos)
  st.session_state["-ADD-"] = ""

# -------- WEB BUILD

st.title("My To-Do App")
st.subheader(get_count())

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todos.pop(index)
    functions.gui_write_todos(todos)
    del st.session_state[todo]
    st.rerun()

st.text_input(label="", placeholder="Add new To-Do...", key="-ADD-", on_change=add_todo)

st.text(get_date())

# For testing
# st.session_state