import streamlit as st
import json
import random

# Завантаження даних з JSON файлів
def load_data(akkusativ_file, dativ_file):
    with open(akkusativ_file, 'r', encoding='utf-8') as file:
        akkusativ_data = json.load(file)["Verben mit Präposition + Akkusativ"]
    with open(dativ_file, 'r', encoding='utf-8') as file:
        dativ_data = json.load(file)["Verben mit Präposition + Dativ"]
    # Об'єднуємо словники
    return {**akkusativ_data, **dativ_data}

# Отримання випадкового дієслова зі списку
def get_random_verb(verbs_dict):
    verbs = list(verbs_dict)
    verb = random.choice(verbs)
    return verb, verbs_dict[verb]

# Шляхи до файлів JSON
akkusativ_file_path = 'akkusativ_verbs_full_translations.json'
dativ_file_path = 'dativ_verbs_with_prepositions.json'

# Завантажуємо дані з файлів
verbs_data = load_data(akkusativ_file_path, dativ_file_path)

# Створення веб-додатку з використанням Streamlit
st.title("Вивчення німецьких дієслів з прийменниками")

if st.button("Отримати нове дієслово"):
    verb, info = get_random_verb(verbs_data)
    st.session_state['current_verb'] = verb
    st.session_state['current_info'] = info

if 'current_verb' in st.session_state:
    verb = st.session_state['current_verb']
    info = st.session_state['current_info']
    if 'translation' in info:
        st.write(f"Дієслово: {verb} - {info['translation']}")
        st.write(f"Відмінок: {info['case']} - Прийменник: {info['preposition']}")
        user_preposition = st.text_input("Введіть прийменник")

        if st.button("Перевірити відповідь"):
            if user_preposition == info['preposition']:
                st.success("Вірно!")
            else:
                st.error(f"Неправильно. Правильна відповідь: {verb} ({info['case']} {info['preposition']})")
    else:
        st.error("Виникла помилка: дані про дієслово не повні.")
