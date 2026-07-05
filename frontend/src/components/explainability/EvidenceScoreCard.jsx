import {
Card,
CardContent,
Typography,
Chip,
Stack
} from "@mui/material";

export default function EvidenceScoreCard(){

return(

<Card>

<CardContent>

<Typography variant="h5" gutterBottom>

Evidence Quality

</Typography>

<Stack spacing={2}>

<Chip color="success" label="FDA Evidence : High"/>

<Chip color="primary" label="CIViC : High"/>

<Chip color="warning" label="COSMIC : Medium"/>

<Chip color="secondary" label="ClinVar : High"/>

<Chip label="OncoKB : Medium"/>

</Stack>

</CardContent>

</Card>

)

}