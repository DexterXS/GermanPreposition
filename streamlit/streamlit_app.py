import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


class StyledButton:
    def __init__(self, label, font_size):
        self.label = label
        self.font_size = font_size

    def render(self):
        button_clicked = st.sidebar.button(self.label, key=self.label.lower().replace(" ", "_"),
                                           style=f"font-size: {self.font_size};")
        return button_clicked


def main():
    st.title("Many Tabs")

    font_size = "16px"  # Adjust the font size as needed

    tab1_button = StyledButton("Tab 1", font_size)
    tab2_button = StyledButton("Tab 2", font_size)
    tab3_button = StyledButton("Tab 3", font_size)

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
