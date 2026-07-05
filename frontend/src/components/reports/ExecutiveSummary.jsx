import {
Card,
CardContent,
Typography
} from "@mui/material";

export default function ExecutiveSummary({pipeline}){

const avg=

pipeline.recommendations.reduce(
(a,b)=>a+b.confidence,0
)/pipeline.recommendations.length;

return(

<Card>

<CardContent>

<Typography variant="h5">

Executive Summary

</Typography>

<Typography mt={2}>

Mutation analysis identified

<b> {pipeline.metadata.gene_count}</b>

gene(s) with

<b> {pipeline.recommendations.length}</b>

recommended therapies.

</Typography>

<Typography mt={2}>

Average AI confidence

<b> {(avg*100).toFixed(1)}%</b>

</Typography>

<Typography mt={2}>

Supporting Literature

<b> {pipeline.literature.length}</b>

</Typography>

<Typography>

Clinical Trials

<b> {pipeline.clinical_trials.length}</b>

</Typography>

</CardContent>

</Card>

)

}