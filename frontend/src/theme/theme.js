import { createTheme } from "@mui/material/styles";

const theme = createTheme({

  palette: {

    primary: {

      main: "#1565C0",

    },

    secondary: {

      main: "#00ACC1",

    },

    background: {

      default: "#F4F6FA",

    },

  },

  typography: {

    fontFamily: "Inter, Roboto, sans-serif",

    h4: {

      fontWeight: 700,

    },

    h5: {

      fontWeight: 700,

    },

    h6: {

      fontWeight: 600,

    },

  },

  shape: {

    borderRadius: 12,

  },

});

export default theme;