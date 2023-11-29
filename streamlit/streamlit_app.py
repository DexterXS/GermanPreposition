import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


def main():
    st.title("many tabs")

    tabs = ["tab 1", "tab 2", "tab 3"]
    selected_tab = st.sidebar.radio("Select tab", tabs)

    if selected_tab == "tab 1":
        tab1_content()

    elif selected_tab == "tab 2":
        tab2_content()

    elif selected_tab == "tab 3":
        tab3_content()


if __name__ == "__main__":
    main()
