import { Box, Button, Typography } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import axios from "axios";

const ChuckNoris = () => {
  const [joke, setJoke] = useState(null);

  const getJoke = async () => {
    const response = await axios.get("https://api.chucknorris.io/jokes/random");
    const responseData = response.data;
    setJoke(responseData.value);
  };

  useEffect(() => {
    getJoke();
  }, []);

  return (
    <Container>
      <Box sx={{ justifyContent: "center", display: "flex", my: 7 }}>
        <img
          style={{ width: "215px" }}
          src="https://freepngimg.com/download/chuck_norris/97563-chuck-norris-free-photo.png"
          alt="chuck-norris"
        />
      </Box>
      {joke && (
        <Box
          sx={{
            justifyContent: "center",
            display: "flex",
            my: 5,
          }}
        >
          <Typography color={"#1976d2"} fontWeight={"bold"} fontSize={"30px"}>
            {joke}
          </Typography>
        </Box>
      )}
      <Box sx={{ justifyContent: "center", display: "flex", my: 7 }}>
        <Button variant="contained" onClick={() => getJoke()}>
          Get Another Joke
        </Button>
      </Box>
    </Container>
  );
};

export default ChuckNoris;
