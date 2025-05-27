import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "fill_in_blanks_streamlit",  # Unique name for the component
        url="http://localhost:3001",  # URL of Vite dev server (matches your package.json PORT)
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(
        parent_dir, "frontend/dist"
    )  # Vite outputs to 'dist' by default
    _component_func = components.declare_component(
        "fill_in_blanks_streamlit", path=build_dir
    )


def fill_in_blanks(segments, options, theme=None, key=None):
    """
    Streamlit component to render a fill-in-the-blanks exercise.

    Parameters
    ----------
    segments : list of lists of str
        Each inner list represents a sentence row.
        e.g., [["Text before blank 1", "text after blank 1, before blank 2", ...]]
    options : list of dicts
        Each dict should have 'id' and 'label'.
        e.g., [{"id": "word1", "label": "Word 1"}]
    theme : dict, optional
        A dictionary to customize the appearance.
        Keys: primaryColor, secondaryBackgroundColor, textColor, font.
    key : str, optional
        Streamlit key for the component.

    Returns
    -------
    dict
        A dictionary representing the placed items in the blanks.
        e.g. {0: {0: "played", 1: "enjoyed"}, 1: {0: "play"}}
        Outer key is row index, inner key is blank index within the row.
    """
    component_value = _component_func(
        segments=segments,
        options=options,
        theme=theme,
        key=key,
        default={},  # Default empty state
    )
    return component_value


# For testing during development
if not _RELEASE:
    import streamlit as st

    st.set_page_config(layout="wide")

    st.subheader("Fill in the Blanks Component Demo")

    custom_theme = {
        "primaryColor": "teal",  # Example: Streamlit's primary color
        "secondaryBackgroundColor": "rgb(240, 242, 246)",  # Example: Streamlit's secondary bg
        "textColor": "rgb(49, 51, 63)",  # Example: Streamlit's text color
        "font": "sans-serif",
    }

    segments_data = [
        ["Yesterday I ", " playing football and I ", " it very much", ""],
        ["Nice I love to ", " football as well"],
        ["The quick brown ", " jumps over the lazy ", "."],
    ]
    options_data = [
        {"id": "play", "label": "play"},
        {"id": "played", "label": "played"},
        {"id": "enjoy", "label": "enjoy"},
        {"id": "enjoyed", "label": "enjoyed"},
        {"id": "fox", "label": "fox"},
        {"id": "dog", "label": "dog"},
        {"id": "cat", "label": "cat"},
    ]

    st.write("### Component with Default Streamlit Theme (via `st.theme`)")
    # Streamlit passes its theme automatically if `theme` prop is not explicitly set to null
    # or another value. For this to work, your React component needs to be able
    # to receive and use `props.theme`. Your `src/components.jsx` already does this.
    value_st_theme = fill_in_blanks(segments_data, options_data, key="fib_st_theme")
    st.write("Returned value (Streamlit theme):")
    st.json(value_st_theme)

    st.markdown("---")

    st.write("### Component with Custom Theme Passed as Prop")
    value_custom_theme = fill_in_blanks(
        segments_data, options_data, theme=custom_theme, key="fib_custom_theme"
    )
    st.write("Returned value (Custom theme):")
    st.json(value_custom_theme)

    st.markdown("---")
    st.write("### Component with No Theme (Fallback to component's internal default)")
    # To truly use no theme from Streamlit and rely on internal defaults,
    # you might need to explicitly pass theme={null} or handle it in MyComponent.
    # However, your FillInBlanks.jsx has its own default theme logic if props.theme is undefined.
    value_no_theme = fill_in_blanks(
        segments_data, options_data, theme=None, key="fib_no_theme"
    )
    st.write("Returned value (No theme / Fallback):")
    st.json(value_no_theme)
