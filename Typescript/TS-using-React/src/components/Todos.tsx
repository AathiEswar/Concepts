
import React, { ReactElement } from 'react';

// React.FC tells that it is a generic type of react component 
const Todos: React.FC<{items : string[] , children? : ReactElement | string }> = (props) => {
  return (
    <div>
      <ul>
        {
            props.items.map(item => <li> {item}</li>) 
            
        }
      </ul>
    </div>
  );
}

export default Todos
