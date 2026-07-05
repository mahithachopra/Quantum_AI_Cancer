import {
Card,
CardContent,
Typography
} from "@mui/material";

export default function LiteratureSection({pipeline}){

return(

<Card>

<CardContent>

<Typography variant="h5">

Top Literature

</Typography>

{pipeline.literature.slice(0,5).map((p,i)=>(

<Typography key={i} mt={2}>

• {p.title}

</Typography>

))}

</CardContent>

</Card>

)

}