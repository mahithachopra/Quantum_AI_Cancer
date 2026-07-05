import {
Card,
CardContent,
Typography,
LinearProgress,
Stack
} from "@mui/material";

const scores=[

["Mutation Evidence",35],

["Clinical Evidence",25],

["Literature",15],

["Clinical Trials",15],

["Knowledge Base",10]

];

export default function ConfidenceBreakdown(){

return(

<Card>

<CardContent>

<Typography variant="h5" gutterBottom>

Confidence Breakdown

</Typography>

<Stack spacing={3}>

{scores.map(([title,val])=>(

<div key={title}>

<Typography>

{title}

</Typography>

<LinearProgress

variant="determinate"

value={val}

/>

<Typography>

{val}%

</Typography>

</div>

))}

</Stack>

</CardContent>

</Card>

)

}