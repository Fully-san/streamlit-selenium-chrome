from bs4 import BeautifulSoup
import requests
import streamlit as st
import os, sys

url = 'http://example.com'

page = requests.get(url)
soup = BeautifulSoup(page.content , 'html.parser')
st.write(soup)