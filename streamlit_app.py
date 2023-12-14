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

if category == 'Akkusativ':
    verbs_data = load_data(akkusativ_file_path)
elif category == 'Dativ':
    verbs_data = load_data(dativ_file_path)

if 'current_verb' not in st.session_state or st.button("Отримати нове дієслово"):
    verb, info = get_random_verb(verbs_data)
    st.session_state['current_verb'] = verb
    st.session_state['current_info'] = info

if 'current_verb' in st.session_state:
    verb = st.session_state['current_verb']
    info = st.session_state['current_info']
    st.write(f"Дієслово: {verb} - {info['translation']}")

    user_case = st.selectbox("Виберіть відмінок", ["Dativ", "Akkusativ"])
    user_preposition = st.text_input("Введіть прийменник")

    if st.button("Перевірити відповідь"):
        if user_case == info['case'] and user_preposition == info['preposition']:
            st.success("Вірно!")
        else:
            st.error(f"Неправильно. Правильна відповідь: {verb} ({info['case']} {info['preposition']})")
