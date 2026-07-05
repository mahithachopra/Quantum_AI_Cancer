import {
Card,
CardContent,
Typography,
Switch,
FormControlLabel
} from "@mui/material";

export default function NotificationSettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
Notifications
</Typography>

<FormControlLabel
control={<Switch defaultChecked/>}
label="Analysis Completed"
/>

<FormControlLabel
control={<Switch defaultChecked/>}
label="New Clinical Trials"
/>

<FormControlLabel
control={<Switch/>}
label="Weekly Reports"
/>

</CardContent>

</Card>

);

}