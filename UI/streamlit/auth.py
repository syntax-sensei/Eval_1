import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

name, authentication_status, username = authenticator.login('Login', 'main')