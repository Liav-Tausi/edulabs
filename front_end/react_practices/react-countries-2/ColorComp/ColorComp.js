import { useState } from "react";

const ColorComp = (props) => {
  const [color, setColor] = useState("#FFFFFF");


  return (
    <form style={{ margin: "100px" }}
     onSubmit={(event) => {
      event.preventDefault();
      props.handleSetColor(color);
      }}>
      <input
        type="color"
        value={color}
        onChange={(event) => setColor(event.target.value)}
      ></input>
      <button type="submit">Change color</button>
    </form>
  );
};

export default ColorComp;
