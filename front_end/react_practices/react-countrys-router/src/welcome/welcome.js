import { Container, Typography, Box } from "@mui/material";

const Welcome = () => {
  return (
    <Container>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          my: 20,
        }}
      >
        <Typography fontSize="65px">Welcome to this random app</Typography>
      </Box>
    </Container>
  );
};

export default Welcome;
