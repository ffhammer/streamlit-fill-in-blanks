import React, { useState, useEffect } from "react";
import { DndContext } from "@dnd-kit/core";
import { Draggable } from "./Draggable";
import { Droppable } from "./Droppable";

function FillInBlanks({ segments, options, theme, onChange }) {
  const currentTheme = theme || {
    primaryColor: 'orange',
    secondaryBackgroundColor: '#f0f2f6',
    textColor: '#333333',
    font: 'sans-serif',
  };

  const [placed, setPlaced] = useState(
    segments.map(row => Object.fromEntries(row.slice(1).map((_, i) => [i, null])))
  );

 useEffect(() => {
    onChange(placed);
  }, [placed, onChange])
  function handleDragEnd({ active, over }) {
    setPlaced(p => {
      const next = p.map(r => ({ ...r }));
      next.forEach(r => {
        for (const k in r) if (r[k] === active.id) r[k] = null;
      });
      if (over) {
        const [ri, ci] = over.id.split("-").map(Number);
        next[ri][ci] = active.id;
      }
      return next;
    });
  }

  return (
    <DndContext onDragEnd={handleDragEnd}>
      <div style={{ display: "flex", flexDirection: "column", gap: 16, alignItems: "center" }}>
        {segments.map((row, ri) => (
          <div
            key={ri}
            style={{ display: "flex", alignItems: "center", gap: 8, width: "100%", maxWidth: 700, justifyContent: "flex-start" }}
          >
            {row.map((text, ci) => (
              <React.Fragment key={ci}>
                {!(text === "" && ci === row.length - 1) && (
                  <div
                    style={{
                      backgroundColor: currentTheme.secondaryBackgroundColor,
                      color: currentTheme.textColor,
                      padding: "6px 10px",
                      borderRadius: 8,
                      fontFamily: currentTheme.font,
                    }}
                  >
                    {text}
                  </div>
                )}
                {ci < row.length - 1 && (
                  <Droppable id={`${ri}-${ci}`} theme={currentTheme}>
                    {placed[ri] && placed[ri][ci] && ( 
                      <Draggable id={placed[ri][ci]} theme={currentTheme}>
                        {options.find(o => o.id === placed[ri][ci])?.label} 
                      </Draggable>
                    )}
                  </Droppable>
                )}
              </React.Fragment>
            ))}
          </div>
        ))}
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap", justifyContent: "center" }}>
          {options
            .filter(o => !placed.some(r => r && Object.values(r).includes(o.id))) 
            .map(o => (
              <Draggable key={o.id} id={o.id} theme={currentTheme}>
                {o.label}
              </Draggable>
            ))}
        </div>
      </div>
    </DndContext>
  );
}

export default FillInBlanks;