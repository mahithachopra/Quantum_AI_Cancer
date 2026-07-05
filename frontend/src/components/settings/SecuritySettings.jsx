import {
Card,
CardContent,
Typography,
Button,
Stack
} from "@mui/material";

export default function SecuritySettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
Security
</Typography>

<Stack spacing={2} mt={2}>

<Button variant="outlined">
Change Password
</Button>

<Button variant="outlined">
Enable 2FA
</Button>

<Button color="error">
Logout
</Button>

</Stack>

</CardContent>

</Card>

);

}