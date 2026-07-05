import {
Card,
CardContent,
Typography,
Switch,
FormControlLabel
} from "@mui/material";

export default function AppearanceSettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
Appearance
</Typography>

<FormControlLabel
control={<Switch />}
label="Dark Mode"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Compact Layout"
/>

</CardContent>

</Card>

);

}