import {
  Typography,
  Container,
  Box,
  Button,
  CircularProgress,
} from "@mui/material";
import axios from "axios";
import { useLocation, Link, useParams } from "react-router-dom";
import { useState, useEffect } from "react";

const Country = () => {
  const [loading, setloading] = useState(false);
  const [returnedData, setReturnedData] = useState(null);
  let { state } = useLocation();
  const { countryId } = useParams();

  useEffect(() => {
    {
      state ? getCountry(state) : getCountry(countryId);
    }
  }, []);

  const getCountry = async (value) => {
    setloading(true);
    const invalidChars = /[$#=@!+%^&*{}()]/;
    try {
      if (!invalidChars.test(value)) {
        const response = await axios.get(
          `https://restcountries.com/v3.1/name/${value}`
        );

        if (response.status <= 400) {
          setloading(false);
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

  return (
    <Container>
      {loading && (
        <Box sx={{ display: "flex", justifyContent: "center", my: 30 }}>
          <CircularProgress />
        </Box>
      )}
      {returnedData && (
        <Box>
          <Typography
            sx={{ display: "flex", justifyContent: "center", my: 6 }}
            fontSize={"35px"}
          >
            <strong>{returnedData[0].name.common}</strong>
          </Typography>
          <img
            src={returnedData[0].flags.svg}
            alt="flag"
            style={{
              display: "flex",
              justifyContent: "center",
              width: "350px",
              margin: "auto",
              borderRadius: "20px",
            }}
          ></img>
          <Box
            sx={{
              mt: 6,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              gap: 2,
              mx: "auto",
            }}
          >
            <Typography variant="h6" align="center">
              <strong>Population:</strong> {returnedData[0].population}
              <br style={{ marginTop: "12px" }} />
              <strong>Capital :</strong> {returnedData[0].capital}
              <br style={{ marginTop: "12px" }} />
              <strong>Language:</strong>{" "}
              {Object.values(returnedData[0].languages)[0]}
              <br style={{ marginTop: "12px" }} />
              <strong>Region:</strong> {returnedData[0].region}
              <br style={{ marginTop: "12px" }} />
              <strong>Subregion:</strong> {returnedData[0].subregion}
            </Typography>
          </Box>
          <Box sx={{ display: "flex", justifyContent: "center", my: 3 }}>
            <Link to="/country">
              <Button>RETURN</Button>
            </Link>
          </Box>
        </Box>
      )}
    </Container>
  );
};

export default Country;
