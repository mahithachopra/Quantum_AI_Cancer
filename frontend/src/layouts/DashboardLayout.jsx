import { Box, Toolbar } from "@mui/material";

import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";

export default function DashboardLayout({
  children,
}) {
  return (
    <Box sx={{ display: "flex" }}>
      <Topbar />

      <Sidebar />

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          ml: "260px",
        }}
      >
        <Toolbar />

        {children}
      </Box>
    </Box>
  );
}