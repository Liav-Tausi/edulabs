import {
  Button,
  Container,
  TextField,
  Typography,
  Grid,
  Box,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import { useState } from "react";
import axios from "axios";
import CountriesPaper from "../CountriesPaper/CountriesPaper";

const Countries = () => {
  const [inputValue, setInputValue] = useState("");
  const [returnedData, setReturnedData] = useState(null);

  const getCountry = async (value) => {
    const invalidChars = /[$#=@!+%^&*{}()]/;
    try {
      if (!invalidChars.test(inputValue)) {
        const response = await axios.get(
          `https://restcountries.com/v3.1/name/${value}`
        );

        if (response.status <= 400) {
          const responseData = response.data;
          setReturnedData(responseData);
        }
      } else {
        alert("bad search");
      }
    } catch (error) {
      console.log(error);
      setReturnedData(-1);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    getCountry(inputValue);
  };

  return (
    <Container>
      <Typography
        sx={{
          display: "flex",
          justifyContent: "center",
          mt: 2,
          fontSize: "20px",
        }}
      >
        Search Countries
      </Typography>
      <Box mt={4}>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            variant="outlined"
            label="Search countries"
            value={inputValue}
            onChange={(event) => setInputValue(event.target.value)}
            InputProps={{
              endAdornment: (
                <Button type="submit">
                  <SearchIcon />
                </Button>
              ),
            }}
          />
        </form>
        {returnedData && returnedData.length >= 1 ? (
          <Grid container spacing={2} mt={4}>
            {returnedData.map((data) => (
              <Grid item xs={12} sm={6} key={data.name.common}>
                <CountriesPaper data={data} />
              </Grid>
            ))}
          </Grid>
        ) : (
          returnedData === -1 && (
            <Box
              sx={{
                display: "flex",
                justifyContent: "center",
                my: 3,
                fontSize: "13px",
                border: "solid 1px red",
                p: 2,
                color: "red",
              }}
            >
              No Countries Found
            </Box>
          )
        )}
      </Box>
    </Container>
  );
};

export default Countries;
