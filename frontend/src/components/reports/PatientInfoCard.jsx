import {
Card,
CardContent,
Typography,
Grid
} from "@mui/material";

export default function PatientInfoCard({pipeline}){

return(

<Card>

<CardContent>

<Typography variant="h5" gutterBottom>

Patient Information

</Typography>

<Grid container spacing={3}>

<Grid size={{xs:6,md:3}}>
<Typography color="text.secondary">
Genes
</Typography>

<Typography fontWeight="bold">
{pipeline.metadata.gene_count}
</Typography>
</Grid>

<Grid size={{xs:6,md:3}}>
<Typography color="text.secondary">
Recommendations
</Typography>

<Typography fontWeight="bold">
{pipeline.recommendations.length}
</Typography>
</Grid>

<Grid size={{xs:6,md:3}}>
<Typography color="text.secondary">
Generated
</Typography>

<Typography fontWeight="bold">
{pipeline.metadata.generated_at.slice(0,10)}
</Typography>
</Grid>

<Grid size={{xs:6,md:3}}>
<Typography color="text.secondary">
Pipeline
</Typography>

<Typography fontWeight="bold">
{pipeline.metadata.pipeline_version}
</Typography>
</Grid>

</Grid>

</CardContent>

</Card>

)

}