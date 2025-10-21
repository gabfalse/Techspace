import { Button, Box, Typography } from "@mui/material";

export default function HomePage() {
  return (
    <Box className="bg-cosmic min-h-screen flex flex-col items-center justify-center text-center">
      <Typography variant="h3" fontWeight="bold" gutterBottom>
        Welcome to Techspace Indonesia🪐
      </Typography>
      <Typography className="text-muted mb-6"></Typography>

      <Button variant="contained" color="primary">
        Join Now
      </Button>
    </Box>
  );
}
