import streamlit as st


def calculator():
    st.title("Компактный калькулятор")

    col1, col2, col3, col4 = st.beta_columns(4)

    with col1:
        num1 = st.button("1")
        num4 = st.button("4")
        num7 = st.button("7")
        num0 = st.button("0")

    with col2:
        num2 = st.button("2")
        num5 = st.button("5")
        num8 = st.button("8")
        dot = st.button(".")

    with col3:
        num3 = st.button("3")
        num6 = st.button("6")
        num9 = st.button("9")
        equals = st.button("=")

    with col4:
        add_btn = st.button("+")
        subtract_btn = st.button("-")
        multiply_btn = st.button("*")
        divide_btn = st.button("/")

    result = st.empty()

    expression = ""
    while True:
        clicked_btn = st.experimental_get_query_params().get("button", [None])[0]

        if clicked_btn is not None:
            if clicked_btn == "=":
                try:
                    result_value = eval(expression)
                    result.success(f"Result: {result_value}")
                except:
                    result.error("Error solve")
                expression = ""
            else:
                expression += clicked_btn


if __name__ == "__main__":
    calculator()
