import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


class StyledButton:
    def __init__(self, label):
        self.label = label

    def render(self):
        key = self.label.lower().replace(" ", "_")
        button_clicked = st.sidebar.button(self.label, key=key, use_container_width=True)
        return button_clicked


def create_buttons(labels):
    for label in labels:
        key = label.lower().replace(" ", "_")
        if st.sidebar.button(label, key=key, use_container_width=True):
            st.sidebar.write(f"Натиснута кнопка: {label}")


def main():
    st.set_page_config(layout="wide")
    st.title("Many Tabs")

    tabs_and_buttons = [("Вкладка 1", tab1_content),
                        ("Вкладка 2", tab2_content),
                        ("Вкладка 3", tab3_content),
                        ("Перша кнопка", None),
                        ("Друга кнопка", None),
                        ("Третя кнопка", None),
                        ("Четверта кнопка", None)]

    for item_label, content_function in tabs_and_buttons:
        if content_function:
            button = StyledButton(item_label)
            selected = button.render()
            if selected:
                content_function()
        else:
            create_buttons([item_label])


if __name__ == "__main__":
    main()
