import streamlit as st

st.set_page_config(page_title="Streamlit Calculator", layout="centered")
st.title("Calculator")

# Session state initialization
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Button click logic
def press(key):
    if key == "=":
        try:
            expr = st.session_state.expression.replace('x', '*')
            st.session_state.expression = str(eval(expr))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += key

# Keyboard input sync
def handle_input():
    st.session_state.expression = st.session_state.input_box
    press("=")

# Input box (keyboard typing support)
st.text_input(
    "Type here and press Enter (or use buttons):",
    value=st.session_state.expression,
    key="input_box",
    on_change=handle_input
)

# Button display mapping (emojis/symbols)
symbol_map = {
    "+": "➕", "-": "➖", "x": "✖", "/": "➗",
    "=": "=", ".": ".",
    "0": "0", "1": "1", "2": "2", "3": "3",
    "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9"
}

# Calculator layout
layout = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "x"],
    [".", "0", "=", "/"]
]

# Render calculator buttons in rows like a mobile calculator
for row_idx, row in enumerate(layout):
    cols = st.columns(len(row), gap="small")
    for col_idx, key in enumerate(row):
        display = symbol_map[key]
        btn_key = f"btn_{row_idx}{col_idx}{key}"  # Unique key for each button
        if cols[col_idx].button(display, key=btn_key):
            press(key)

# Clear button with some spacing
st.markdown("###")
st.button("Clear", on_click=lambda: st.session_state.update(expression=""), key="clear_button")
