import pandas
import streamlit as st
import math


# st.sidebar.write('Home')
# st.sidebar.write('Contact us')

st.header('The Best Company')
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.subheader('Our Team')

col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

df = pandas.read_csv("data.csv", sep=',')

length = 0
for index, row in df.iterrows():
    length += 1

one = length / 3
one = math.floor(one)
x1 = length - one


with col1:
    for index, row in df[:one].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        # st.subheader(row['first name'])
        st.write(row['role'])
        st.image('004 images/'+ row['image'])


with col2:
    for index, row in df[one:x1].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image('004 images/'+ row['image'])

with col3:
    for index, row in df[x1:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image('004 images/'+ row['image'])

# check1

