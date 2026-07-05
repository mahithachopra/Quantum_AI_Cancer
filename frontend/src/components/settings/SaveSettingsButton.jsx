import {
Card,
CardContent,
Button,
Stack
} from "@mui/material";

export default function SaveSettingsButton(){

const saveSettings=()=>{

alert("Settings saved successfully.");

};

return(

<Card>

<CardContent>

<Stack direction="row" justifyContent="flex-end">

<Button
variant="contained"
size="large"
onClick={saveSettings}
>
Save Settings
</Button>

</Stack>

</CardContent>

</Card>

);

}