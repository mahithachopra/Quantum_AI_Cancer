import {
Card,
CardContent,
Typography,
Stepper,
Step,
StepLabel
} from "@mui/material";

const steps=[

"Mutation Detection",

"Knowledge Base",

"Pathway Analysis",

"Drug Ranking",

"Evidence Aggregation",

"Final Recommendation"

];

export default function DecisionTree(){

return(

<Card>

<CardContent>

<Typography variant="h5">

AI Decision Flow

</Typography>

<Stepper

orientation="vertical"

activeStep={steps.length}

>

{steps.map(step=>(

<Step

completed

key={step}

>

<StepLabel>

{step}

</StepLabel>

</Step>

))}

</Stepper>

</CardContent>

</Card>

)

}