import {
  AppBar,
  Toolbar,
  Typography,
} from "@mui/material";

export default function Topbar() {
  return (
    <AppBar
      position="fixed"
      sx={{
        zIndex: 1201,
      }}
    >
      <Toolbar>
        <Typography
          variant="h6"
          fontWeight="bold"
        >
          Quantum AI Cancer Platform
        </Typography>
      </Toolbar>
    </AppBar>
  );
}