import streamlit as st
from tab1 import tab1_content
from tab2 import tab2_content
from tab3 import tab3_content


def main():
    st.title("Many Tabs")

    tabs = ["Tab 1", "Tab 2", "Tab 3"]
    selected_tab = st.sidebar.selectbox("Select Tab", tabs)

    if selected_tab == "Tab 1":
        tab1_content()
    elif selected_tab == "Tab 2":
        tab2_content()
    elif selected_tab == "Tab 3":
        tab3_content()


if __name__ == "__main__":
    main()
