import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


def main():
    st.title("Many Tabs")

    selected_tab = st.sidebar.button("Tab 1")
    if selected_tab:
        tab1_content()

    selected_tab = st.sidebar.button("Tab 2")
    if selected_tab:
        tab2_content()

    selected_tab = st.sidebar.button("Tab 3")
    if selected_tab:
        tab3_content()


if __name__ == "__main__":
    main()
