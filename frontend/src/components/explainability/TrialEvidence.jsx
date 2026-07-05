import {
Card,
CardContent,
Typography,
List,
ListItem
} from "@mui/material";

export default function TrialEvidence({pipeline}){

const trials=
pipeline?.clinical_trials || [];

return(

<Card>

<CardContent>

<Typography variant="h5">

Supporting Clinical Trials

</Typography>

<List>

{trials.slice(0,5).map((t,i)=>(

<ListItem key={i}>

{t.title || t.brief_title || "Clinical Trial"}

</ListItem>

))}

</List>

</CardContent>

</Card>

)

}