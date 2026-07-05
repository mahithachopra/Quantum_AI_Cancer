import {
Card,
CardContent,
Typography,
Switch,
Stack,
FormControlLabel
} from "@mui/material";

export default function PipelineSettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
Pipeline Modules
</Typography>

<Stack>

<FormControlLabel
control={<Switch defaultChecked />}
label="Mutation Detection"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Knowledge Base"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Drug Ranking"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Clinical Trials"
/>

<FormControlLabel
control={<Switch defaultChecked />}
label="Literature Mining"
/>

</Stack>

</CardContent>

</Card>

);

}