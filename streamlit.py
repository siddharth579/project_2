import streamlit as st
import requests
from datetime import datetime
import pytz

API_URL = 'http://127.0.0.1:5000/api/datetime'

st.title('Current Date & Time App')
choice = st.selectbox('Select what to show', ['Date', 'Time', 'Both'])
timezone = st.text_input('Enter timezone (optional)', '')

if st.button('Get Now'):
    try:
        params = {'type': 'date' if choice == 'Date' else 'time' if choice == 'Time' else 'both'}
        if timezone:
            params['tz'] = timezone
        r = requests.get(API_URL, params=params)
        st.success(f"Backend → {r.json()['value']}")
    except:
        st.warning('Backend not available, computing locally...')
        try:
            if timezone:
                tz = pytz.timezone(timezone)
                now = datetime.now(tz)
            else:
                now = datetime.now()
        except:
            now = datetime.now()
        fmt = '%Y-%m-%d' if choice == 'Date' else '%H:%M:%S' if choice == 'Time' else '%Y-%m-%d %H:%M:%S'
        st.info(f'Local → {now.strftime(fmt)}')