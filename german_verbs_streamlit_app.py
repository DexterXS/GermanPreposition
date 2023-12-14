import streamlit as st
import spacy


def annotate_german_words(text, nlp):
    doc = nlp(text)
    annotated_text = ""

    for token in doc:
        annotations = []

        # Часть речи
        annotations.append(f"POS: {token.pos_}")

        if token.pos_ == "VERB":
            color = "blue"
            font_weight = "normal"
        elif token.pos_ == "NOUN":
            color = "green"
            font_weight = "normal"
        elif token.pos_ == "ADP":
            color = "red"
            font_weight = "normal"
        elif token.pos_ == "PROPN":
            color = "purple"
            font_weight = "normal"
        elif token.pos_ == "DET":
            color = "orange"
            font_weight = "normal"
        elif token.pos_ == "PRON":
            color = "brown"
            font_weight = "normal"
        elif token.pos_ == "AUX":
            color = "teal"
            font_weight = "normal"
        else:
            color = "white"
            font_weight = "normal"

        if token.lang_ == "de":
            annotated_text += f'<span style="color:{color}; font-weight:{font_weight};" title="{", ".join(annotations)}">{token.text}</span> '
        else:
            annotated_text += token.text + " "

    return annotated_text.strip()


def show_colored_legend():
    legend = [
        ("<span style='color: blue;'>VERB</span>: Глагол"),
        ("<span style='color: green;'>NOUN</span>: Существительное"),
        ("<span style='color: red;'>ADP</span>: Предлог"),
        ("<span style='color: purple;'>PROPN</span>: Имя собственное"),
        ("<span style='color: orange;'>DET</span>: Артикль или детерминатив"),
        ("<span style='color: brown;'>PRON</span>: Местоимение"),
        ("<span style='color: teal;'>AUX</span>: Вспомогательный глагол")
    ]

    st.markdown("## Легенда с цветами частей речи")
    for item in legend:
        st.markdown(item, unsafe_allow_html=True)


def load_spacy_model():
    return spacy.load("de_core_news_sm")


def main():
    st.title("Немецкий текст")

    nlp = load_spacy_model()

    input_text = st.text_area("Введите текст:", value="", key="input_text")

    if st.button("Подсветить немецкие слова"):
        sentences = input_text.split(". ")
        highlighted_text = ""

        for sentence in sentences:
            if sentence.strip():  # Пропустим пустые строки
                highlighted_sentence = annotate_german_words(sentence, nlp)
                highlighted_text += f"{highlighted_sentence.strip()}\n"

        st.markdown(f"Подсвеченный текст:\n{highlighted_text}", unsafe_allow_html=True)
        show_colored_legend()


if __name__ == "__main__":
    main()