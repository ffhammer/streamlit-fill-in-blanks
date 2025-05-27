import {useDraggable} from '@dnd-kit/core';

export function Draggable({id, children, theme, freeze}) {
  const {attributes, listeners, setNodeRef, transform} = useDraggable({
    id,
    disabled: freeze, // Disable dnd-kit draggable if frozen
  });

  const currentTheme = theme || {
    primaryColor: 'orange',
    textColor: '#333333', // This is for body text, primaryColor buttons usually have white text
    font: 'sans-serif',
  };

  const style = {
    transform: transform ? `translate(${transform.x}px, ${transform.y}px)` : undefined,
    backgroundColor: currentTheme.primaryColor,
    color: '#FFFFFF', // White text on primary color background
    fontFamily: currentTheme.font,
    border: 'none',
    borderRadius: '8px',
    padding: '8px 12px', // Consistent padding
    minHeight: '40px', // Consistent height
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    cursor: freeze ? 'default' : 'grab', // Change cursor if frozen
    touchAction: 'none', // Recommended for better mobile dragging
    opacity: freeze ? 0.7 : 1, // Optionally make it look a bit disabled
  };
  
  // Conditionally apply listeners and attributes
  const dragHandlers = freeze ? {} : {...listeners, ...attributes};

  return (
    <button ref={setNodeRef} style={style} {...dragHandlers}>
      {children}
    </button>
  );
}
