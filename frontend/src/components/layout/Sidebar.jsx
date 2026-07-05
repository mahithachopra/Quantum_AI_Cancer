import {
  Drawer,
  Toolbar,
  List,
  ListItemButton,
  ListItemText,
} from "@mui/material";

import {
  Link,
  useLocation,
} from "react-router-dom";

const drawerWidth = 260;

const menu = [
  {
    text: "Dashboard",
    path: "/",
  },
  {
    text: "Mutation Analysis",
    path: "/mutation",
  },
  {
    text: "Recommendations",
    path: "/recommendations",
  },
  {
    text: "Clinical Trials",
    path: "/trials",
  },
  {
    text: "Literature",
    path: "/literature",
  },
  {
    text: "Reports",
    path: "/reports",
  },
  {
    text: "Explainability",
    path: "/explainability",
  },
  {
    text: "Settings",
    path: "/settings",
  },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
        },
      }}
    >
      <Toolbar />

      <List>
        {menu.map((item) => (
          <ListItemButton
            key={item.path}
            component={Link}
            to={item.path}
            selected={
              location.pathname === item.path
            }
          >
            <ListItemText
              primary={item.text}
            />
          </ListItemButton>
        ))}
      </List>
    </Drawer>
  );
}