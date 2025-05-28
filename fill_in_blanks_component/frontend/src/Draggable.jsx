import {useDraggable} from '@dnd-kit/core';

export function Draggable({id, children, theme}) {
  const {attributes, listeners, setNodeRef, transform} = useDraggable({id});

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
    cursor: 'grab',
    touchAction: 'none', // Recommended for better mobile dragging
  };

  return (
    <button ref={setNodeRef} style={style} {...listeners} {...attributes}>
      {children}
    </button>
  );
}
