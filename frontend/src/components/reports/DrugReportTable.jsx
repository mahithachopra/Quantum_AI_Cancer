import {
Card,
CardContent,
Typography
} from "@mui/material";

import {
DataGrid
} from "@mui/x-data-grid";

export default function DrugReportTable({pipeline}){

const rows=

pipeline.recommendations.map((r,i)=>({

id:i,

drug:r.drug,

gene:r.gene,

confidence:(r.confidence*100).toFixed(1)+"%",

approved:r.approved?"Yes":"No"

}));

const columns=[

{field:"drug",headerName:"Drug",flex:1},

{field:"gene",headerName:"Gene",width:130},

{field:"confidence",headerName:"Confidence",width:160},

{field:"approved",headerName:"FDA",width:120},

];

return(

<Card>

<CardContent>

<Typography variant="h5" gutterBottom>

Recommended Drugs

</Typography>

<div style={{height:450}}>

<DataGrid

rows={rows}

columns={columns}

/>

</div>

</CardContent>

</Card>

)

}