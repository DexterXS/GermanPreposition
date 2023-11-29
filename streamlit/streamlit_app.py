import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


class StyledButton:
    def __init__(self, label, key, width, height, font_size):
        self.label = label
        self.key = key
        self.width = width
        self.height = height
        self.font_size = font_size

    def render(self):
        return st.sidebar.button(
            self.label,
            key=self.key,
            width=self.width,
            height=self.height,
            css=f"font-size: {self.font_size};"
        )


def main():
    st.title("Many Tabs")

    button_width = 150  # Adjust the width of the buttons as needed
    font_size = "16px"  # Adjust the font size as needed

    tab1_button = StyledButton("Tab 1", "tab1", button_width, 50, font_size)
    tab2_button = StyledButton("Tab 2", "tab2", button_width, 50, font_size)
    tab3_button = StyledButton("Tab 3", "tab3", button_width, 50, font_size)

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
