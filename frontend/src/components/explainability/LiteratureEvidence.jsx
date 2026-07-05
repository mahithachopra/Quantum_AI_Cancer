import {
Card,
CardContent,
Typography,
List,
ListItem
} from "@mui/material";

export default function LiteratureEvidence({pipeline}){

const papers=
pipeline?.literature || [];

return(

<Card>

<CardContent>

<Typography variant="h5">

Supporting Literature

</Typography>

<List>

{papers.slice(0,5).map((p,i)=>(

<ListItem key={i}>

{p.title || "Research Paper"}

</ListItem>

))}

</List>

</CardContent>

</Card>

)

}