import streamlit as st


st.write("""
#Finding the largest among the 3 given numbers(value greater than the other two).
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():

    Input1 = st.number_input("Input 1",min_value=0.0,max_value=2000000.0)
    Input2 = st.number_input("Input 2",min_value=0.0,max_value=2000000.0)
    Input3 = st.number_input("Input 3",min_value=0.0,max_value=2000000.0)
   
    return (Input1,Input2,Input3)

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

x=df[0]
y=df[1]
z=df[2]
flag=-1
if x>=y and x>=z:
    flag=0
elif y>=x and y>=z:
    flag=1
else:
    flag=2


st.subheader('Greatest of 3 Numbers is')
st.write(df[flag])
