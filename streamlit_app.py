import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
streamlit.header('Fruityvice Fruit Advice!')
# streamlit.text(fruityvice_response.json())
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get info")
  else:
    streamlit.write('The user entered:', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
  
except URLError as e:
  streamlit.error()
  
streamlit.stop()  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
streamlit.text_input('What fruit would you like to add?')
