from bs4 import BeautifulSoup
import requests
import streamlit as st
import os, sys

url = 'https://marvelsnapzone.com/news/patch-notes/'

page = requests.get(url)
soup = BeautifulSoup(page.text , 'html.parser')
st.write(soup.prettify())