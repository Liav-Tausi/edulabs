import { Link } from "react-router-dom";
import { ListItem, Paper, List } from "@mui/material";

const CountriesPaper = (props) => {
  const [loading, setloading] = useState(false);
  return (
    <Link
      to={`/country/${props.data.name.common}`}
      state={props.data.name.common}
      style={{ textDecoration: "none" }}
    >
      <Paper
        elevation={3}
        sx={{
          display: "flex",
          justifyContent: "center",
          p: 2,
          "&:hover": {
            transform: "scale(0.992)",
            cursor: "pointer",
          },
        }}
      >
        <List>
          <ListItem sx={{ display: "flex", justifyContent: "center" }}>
            <strong>{props.data.name.common}</strong>
          </ListItem>
          <ListItem sx={{ display: "flex", justifyContent: "center" }}>
            <img
              src={props.data.flags.svg}
              alt="flag"
              style={{
                width: "40px",
                marginTop: "10px",
              }}
            ></img>
          </ListItem>
        </List>
      </Paper>
    </Link>
  );
};

export default CountriesPaper;
