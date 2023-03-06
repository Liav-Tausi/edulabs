import { Box, Typography } from "@mui/material";

const NoMatch = () => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        my: 20,
      }}
    >
      <Typography sx={{ fontSize: "100px" }}>404!</Typography>
    </Box>
  );
};

export default NoMatch;
