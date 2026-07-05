import {
Card,
CardContent,
Typography,
Switch,
FormControlLabel,
Slider
} from "@mui/material";

export default function AISettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
AI Configuration
</Typography>

<FormControlLabel
control={<Switch defaultChecked />}
label="Enable AI Ranking"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Enable Explainability"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Use Literature Mining"
/>

<Typography mt={2}>
Minimum Confidence
</Typography>

<Slider
defaultValue={70}
valueLabelDisplay="auto"
/>

</CardContent>

</Card>

);

}