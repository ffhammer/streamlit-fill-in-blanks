import React, { useEffect } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import FillInBlanks from "./FillinBlanks"; 

function MyComponent({ args, theme }) {
  const { segments = [], options = [], freeze = false } = args;
  const handleChange = placed => Streamlit.setComponentValue(placed);

  useEffect(() => {
    Streamlit.setFrameHeight();
  }, [segments, options, theme, freeze]);

  return (
    <FillInBlanks
      segments={segments}
      options={options}
      theme={theme}
      freeze={freeze}
      onChange={handleChange}
    />
  );
}

export default withStreamlitConnection(MyComponent);
