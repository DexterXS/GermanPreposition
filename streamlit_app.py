import streamlit as st
import random

# Розширений словник з дієсловами, перекладами, відмінками та прийменниками
verbs_info = {
    "achten": {"translation": "звертати увагу", "case": "Akkusativ", "preposition": "auf"},
    "ankommen": {"translation": "залежати", "case": "Dativ", "preposition": "auf"},
    "antworten": {"translation": "відповідати", "case": "Dativ", "preposition": "auf"},
    "warten": {"translation": "чекати", "case": "Akkusativ", "preposition": "auf"},
    "sich freuen": {"translation": "радіти", "case": "Akkusativ", "preposition": "auf"}
    # Додайте більше дієслів за бажанням
}

def get_random_verb():
    """Функція для вибору випадкового дієслова."""
    verb, info = random.choice(list(verbs_info.items()))
    return verb, info

# Створення веб-додатку з використанням Streamlit
st.title("Вивчення німецьких дієслів з прийменниками")

if st.button("Отримати дієслово"):
    verb, info = get_random_verb()
    st.session_state['current_verb'] = verb
    st.session_state['current_info'] = info
    st.write(f"Дієслово: {verb} - {info['translation']}")

if 'current_verb' in st.session_state:
    verb = st.session_state['current_verb']
    info = st.session_state['current_info']

    user_case = st.selectbox("Виберіть відмінок", ["Dativ", "Akkusativ"])
    user_preposition = st.text_input("Введіть прийменник")

    if st.button("Перевірити відповідь"):
        if user_case == info['case'] and user_preposition == info['preposition']:
            st.success("Вірно!")
        else:
            st.error(f"Неправильно. Правильна відповідь: {verb} ({info['case']} {info['preposition']})")
