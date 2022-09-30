import streamlit
import pandas
streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Bagel & Omlett')
streamlit.text('🥗Bluberry Pancakes')
streamlit.text('🥣Raagi Pour')
streamlit.header('🍌🥭Make your own smoothie🥝🍇')

my_first_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect('Pick some fruits:',list(my_first_list.index))
streamlit.dataframe(my_first_list)
