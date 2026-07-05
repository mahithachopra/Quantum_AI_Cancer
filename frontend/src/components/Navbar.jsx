import { AppBar, Toolbar, Typography } from "@mui/material";
import LocalHospitalIcon from "@mui/icons-material/LocalHospital";

export default function Navbar() {

    return (

        <AppBar position="static">

            <Toolbar>

                <LocalHospitalIcon sx={{ mr: 2 }} />

                <Typography
                    variant="h6"
                    sx={{ fontWeight: "bold" }}
                >

                    Quantum AI Cancer Recommendation System

                </Typography>

            </Toolbar>

        </AppBar>

    );

}