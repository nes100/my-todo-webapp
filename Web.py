import streamlit as st
import functions

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "DatabaseSample.xlsx"

todos = functions.read()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)

st.title("My Todo App ")
st.subheader("This is my todo list for today")
st.date_input("Date")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
         todos.pop(index)
         functions.write(todos)
         del st.session_state[todo]
         st.experimental_rerun()

st.text_input(label=" ",placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")

