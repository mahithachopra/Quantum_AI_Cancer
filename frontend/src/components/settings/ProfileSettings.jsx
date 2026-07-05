import {
Card,
CardContent,
Typography,
Stack,
TextField
} from "@mui/material";

export default function ProfileSettings(){

return(

<Card>

<CardContent>

<Typography variant="h5" mb={2}>
Profile
</Typography>

<Stack spacing={2}>

<TextField
label="Clinician Name"
defaultValue="Dr. John Doe"
/>

<TextField
label="Hospital"
defaultValue="Quantum Cancer Center"
/>

<TextField
label="Department"
defaultValue="Precision Oncology"
/>

</Stack>

</CardContent>

</Card>

);

}