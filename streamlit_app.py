import streamlit
import pandas
import requests
streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Bagel & Omlett')
streamlit.text('🥗Bluberry Pancakes')
streamlit.text('🥣Raagi Pour')
streamlit.header('🍌🥭Make your own smoothie🥝🍇')

my_first_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_first_list = my_first_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruits:',list(my_first_list.index),['Avocado','Honeydew'])
fruits_to_show=my_first_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header('Fruityvice Fruit Advice!')
streamlit.text(fruityvice_response.json())
