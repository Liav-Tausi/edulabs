import { Box, Button, LinearProgress, Stack, Typography } from "@mui/material";
import axios from "axios";
import { useState } from "react";
import FactWithLike from "./FactWithLike";

import LikedList from "./LikedList";

const App = () => {
  const [factData, setFactData] = useState({
    text: null,
    loading: false,
  });
  const [likedNumbers, setLikedNumbers] = useState([]);
  const [lastLikedNum, setlastLikedNum] = useState(null)
  const [p, setP] = useState('');
  const [selected, setSelected] = useState(null)

 
  const getFact = async () => {
    setFactData({ ...factData, loading: true });
    setlastLikedNum(null)
    try {
      const response = await axios.get("http://numbersapi.com/random/math");
      const responseData = response;
      setFactData({
        text: responseData.data,
        loading: false,
      });
    } catch (error) {
      console.log(error);
    }
  };

  const handleLikedNumber = (number) => {
    const newArray = [...likedNumbers, {data: factData.text, number: number}]
    setLikedNumbers(newArray)
    setlastLikedNum(number) 
  }

  const handleLikedClicked = (fact) => {
    setP(fact)
    if (selected === null) {
      setSelected(1) 
    } else if (fact !== p) {
      setP(fact)
    }
    else{
      setSelected(null)
      setP(null)
    }
  }

  const handleDeleteCliced = (number) => {
    const updatedNumbers = likedNumbers.filter((n) => n.number !== number);
    setLikedNumbers(updatedNumbers)
    if (lastLikedNum === number) {
      setlastLikedNum(false)
    }   
    setP('')
  }

  return (
    <Box
      sx={{
        width: "50%",
        margin: "auto",
        marginTop: "1em",
      }}
    >
      <h2 align="center">Welcome to Numbers Facts!</h2>

      <Stack spacing={2} marginY="2rem">
        <Button variant="contained" onClick={getFact}>
          GET INTERESTING FACT!
        </Button>
      </Stack>
      {factData.loading &&
       <LinearProgress hidden={!factData.loading} />}

      {factData.text && (
        <FactWithLike
          factText={factData.text}
          onLikedNumber={handleLikedNumber}
          isLastNum={lastLikedNum}
        />
      )}
      {likedNumbers.length > 0 && (
        <Stack spacing={2} marginY="1em" sx={{justifyContent: "center"}}>
          <hr />
          <h5>Numbers you liked:</h5>
          <LikedList 
            numbers={likedNumbers}
            onClick={handleLikedClicked}
            onDelete={handleDeleteCliced} />
        </Stack>  
      )}
      {p &&
        <Typography>{p}</Typography>
      }
      
    </Box>
  );
};

export default App;
