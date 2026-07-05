import {
Card,
CardContent,
Typography,
Chip,
Stack
} from "@mui/material";

export default function DatabaseSettings(){

return(

<Card>

<CardContent>

<Typography variant="h5">
Connected Databases
</Typography>

<Stack direction="row" spacing={1} mt={2} flexWrap="wrap">

<Chip label="FDA" color="success"/>

<Chip label="PubMed" color="primary"/>

<Chip label="COSMIC"/>

<Chip label="ClinVar"/>

<Chip label="DrugBank"/>

<Chip label="CIViC"/>

</Stack>

</CardContent>

</Card>

);

}