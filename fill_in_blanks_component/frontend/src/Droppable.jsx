import {useDroppable} from '@dnd-kit/core';

export function Droppable({id, children, theme}) {
  const {isOver, setNodeRef} = useDroppable({id});
  
  const currentTheme = theme || {
    primaryColor: 'orange',
    secondaryBackgroundColor: '#f0f2f6',
    textColor: '#333333',
    font: 'sans-serif',
  };

  const style = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    verticalAlign: 'middle',
    backgroundColor: isOver ? currentTheme.primaryColor : currentTheme.secondaryBackgroundColor,
    minWidth: '60px', // Can be adjusted or made themeable
    minHeight: '40px', // Consistent height
    margin: '0 6px',
    padding: '8px', // Consistent padding
    border: `1px dashed ${isOver ? currentTheme.primaryColor : currentTheme.textColor}`,
    borderRadius: '8px',
    textAlign: 'center',
    color: currentTheme.textColor, // For any potential text content
    fontFamily: currentTheme.font,
  };

  return (
    <div ref={setNodeRef} style={style}>
      {children}
    </div>
  );
}
