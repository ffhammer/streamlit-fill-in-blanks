import streamlit as st
from fill_in_blanks_component import fill_in_blanks

st.set_page_config(layout="wide")
st.subheader("Fill in the Blanks Component Demo")

# --- Options and Theme remain the same ---
options_data = [
    {"id": "play2", "label": "play"},
    {"id": "played", "label": "played"},
    {"id": "enjoy", "label": "enjoy"},
    {"id": "enjoyed", "label": "enjoyed"},
    {"id": "fox", "label": "fox"},
    {"id": "dog", "label": "dog"},
    {"id": "cat", "label": "cat"},
    {"id": "jumped", "label": "jumped"},
    {"id": "ran", "label": "I very long example"},
]
custom_theme = {
    "primaryColor": "teal",
    "secondaryBackgroundColor": "rgb(240, 242, 246)",
    "textColor": "rgb(49, 51, 63)",
    "font": "sans-serif",
}

# --- Example 1: Using the new delimiter-based input ---
sentences_with_delimiters = [
    "Yesterday I $ playing football and I $ it very much$.",  # Blank at the end
    "Nice I love to $ football as well.",
    "The quick brown $ jumps over the lazy $.",
    "Only a blank: $",
]
st.write("### Component with Delimiter-Based Input (Default '$')")
st.write("#### Inputs")
st.write("Sentences:")
st.json(sentences_with_delimiters)
st.write("Options:")
st.json(options_data)

value_delimiter = fill_in_blanks(
    sentences_with_delimiters, options_data, key="fib_delimiter"
)
print(value_delimiter)
st.write("Returned value (Delimiter-based):")
st.json(value_delimiter)
st.markdown("---")

# --- Example 2: Using a custom delimiter ---
sentences_with_custom_delimiter = [
    "The weather is ___ today, perfect for ___.",
    "She ___ to the store and ___ some milk___",  # Blank at the end
]
st.write("### Component with Custom Delimiter ('___')")
st.write("#### Inputs")
st.write("Sentences:")
st.json(sentences_with_custom_delimiter)
st.write("Options:")
st.json(options_data)

value_custom_delimiter = fill_in_blanks(
    sentences_with_custom_delimiter,
    options_data,
    delimiter="___",
    theme=custom_theme,
    key="fib_custom_delimiter",
)

st.write("Returned value (Custom Delimiter):")
st.json(value_custom_delimiter)
st.markdown("---")

# --- Example 3: Original pre-segmented input (for backward compatibility/testing) ---
pre_segmented_data = [
    [
        "Yesterday I ",
        " playing football and I ",
        " it very much",
        "",
    ],  # Explicit empty string for end blank
    ["Nice I love to ", " football as well"],
    ["The quick brown ", " jumps over the lazy ", "."],
]
st.write("### Component with Pre-segmented Input")
st.write("#### Inputs")
st.write("Sentences:")
st.json(pre_segmented_data)
st.write("Options:")
st.json(options_data)

value_pre_segmented = fill_in_blanks(
    pre_segmented_data, options_data, theme=None, key="fib_pre_segmented"
)
st.write("Returned value (Pre-segmented):")
st.json(value_pre_segmented)
