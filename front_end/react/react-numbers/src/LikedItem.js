import { Chip } from "@mui/material";

const LikedItem = (props) => {
  return (
    <Chip
      sx={{
        "&:hover": {
          backgroundColor: "#0275d8",
          color: "black",
          cursor: "pointer",
        },
        "&:active": {
          transform: "scale(0.9)",
        },
      }}
      label={props.number}
      color="primary"
      variant="outlined"
      onDelete={() => props.onDelete(props.number)}
      onClick={() => props.onClick(props.fact)}
    />
  );
};

export default LikedItem;
