import {
Card,
CardContent,
Typography,
Grid
} from "@mui/material";

export default function SystemInformation(){

return(

<Card>

<CardContent>

<Typography variant="h5" mb={2}>
System Information
</Typography>

<Grid container spacing={2}>

<Grid size={{xs:6}}>
AI Engine
</Grid>

<Grid size={{xs:6}}>
Quantum AI v1.0
</Grid>

<Grid size={{xs:6}}>
Backend
</Grid>

<Grid size={{xs:6}}>
FastAPI
</Grid>

<Grid size={{xs:6}}>
Frontend
</Grid>

<Grid size={{xs:6}}>
React + MUI
</Grid>

<Grid size={{xs:6}}>
Pipeline
</Grid>

<Grid size={{xs:6}}>
Active
</Grid>

</Grid>

</CardContent>

</Card>

);

}