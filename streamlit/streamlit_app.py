import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


class StyledButton:
    def __init__(self, label):
        self.label = label

    def render(self):
        button_clicked = st.sidebar.button(self.label, key=self.label.lower().replace(" ", "_"),
                                           use_container_width=True)
        return button_clicked


def main():
    st.set_page_config(layout="wide")
    st.title("Many Tabs")

    tab1_button = StyledButton("Tab 1")
    tab2_button = StyledButton("Tab 2")
    tab3_button = StyledButton("Tab 3")

    selected_tab_1 = tab1_button.render()
    if selected_tab_1:
        tab1_content()

    selected_tab_2 = tab2_button.render()
    if selected_tab_2:
        tab2_content()

    selected_tab_3 = tab3_button.render()
    if selected_tab_3:
        tab3_content()


if __name__ == "__main__":
    main()
