import {
Card,
CardContent,
Typography
} from "@mui/material";

export default function TrialSection({pipeline}){

return(

<Card>

<CardContent>

<Typography variant="h5">

Clinical Trials

</Typography>

{pipeline.clinical_trials.slice(0,5).map((t,i)=>(

<Typography key={i} mt={2}>

• {t.title || t.brief_title}

</Typography>

))}

</CardContent>

</Card>

)

}