import { Stack } from "@mui/material";
import LikedItem from "./LikedItem";

export default function LikedList(props) {
    const items = props.numbers.map((num) => (
    <LikedItem 
        key={num.number}
        fact={num.data}
        number={num.number}
        onClick={props.onClick}
        onDelete={props.onDelete}
    />
  ));

  return (
    <Stack direction="row" spacing={1}>
      {items}
    </Stack>
  );
}
