import streamlit as st
import json
import random

# Завантаження даних з JSON файлу
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Отримання випадкового дієслова зі списку
def get_random_verb(verbs_dict):
    verbs = list(verbs_dict.keys())
    verb = random.choice(verbs)
    return verb, verbs_dict[verb]

# Шляхи до файлів JSON
akkusativ_file_path = 'akkusativ_verbs_full_translations.json'
dativ_file_path = 'dativ_verbs_with_prepositions.json'

# Створення веб-додатку з використанням Streamlit
st.title("Вивчення німецьких дієслів з прийменниками")

# Вибір категорії дієслів
category = st.radio("Виберіть категорію:", ['Akkusativ', 'Dativ'])

# Завантаження даних відповідно до вибору користувача
if category == 'Akkusativ':
    verbs_data = load_data(akkusativ_file_path)
elif category == 'Dativ':
    verbs_data = load_data(dativ_file_path)

if st.button("Отримати дієслово"):
    verb, verb_info = get_random_verb(verbs_data)
    st.session_state['current_verb'] = verb
    st.session_state['current_info'] = verb_info

if 'current_verb' in st.session_state:
    st.write(f"Дієслово: {st.session_state['current_verb']} ({st.session_state['current_info']['case']} {st.session_state['current_info']['preposition']})")
    st.write(f"Переклад: {st.session_state['current_info']['translation']}")
