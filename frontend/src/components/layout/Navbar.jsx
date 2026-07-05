import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Avatar,
  Badge,
  Box,
} from "@mui/material";

import NotificationsIcon from "@mui/icons-material/Notifications";
import SettingsIcon from "@mui/icons-material/Settings";

export default function Navbar() {
  return (
    <AppBar
      position="sticky"
      elevation={1}
      color="inherit"
      sx={{
        zIndex: 1300,
      }}
    >
      <Toolbar>

        <Typography
          variant="h5"
          fontWeight={700}
          color="primary"
          sx={{ flexGrow: 1 }}
        >
          Quantum AI Cancer Platform
        </Typography>

        <Box>

          <IconButton>

            <Badge
              badgeContent={2}
              color="error"
            >
              <NotificationsIcon />
            </Badge>

          </IconButton>

          <IconButton>
            <SettingsIcon />
          </IconButton>

          <Avatar
            sx={{
              ml: 2,
              bgcolor: "primary.main",
            }}
          >
            Q
          </Avatar>

        </Box>

      </Toolbar>
    </AppBar>
  );
}