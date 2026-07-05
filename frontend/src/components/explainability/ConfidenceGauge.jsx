import {
Card,
CardContent,
Typography,
CircularProgress,
Box
} from "@mui/material";

export default function ConfidenceGauge({confidence=0.75}){

return(

<Card>

<CardContent>

<Typography variant="h5">

Overall Confidence

</Typography>

<Box

display="flex"

justifyContent="center"

mt={3}

>

<CircularProgress

variant="determinate"

value={confidence*100}

size={120}

/>

</Box>

<Typography

align="center"

mt={2}

variant="h4"

>

{(confidence*100).toFixed(1)}%

</Typography>

</CardContent>

</Card>

)

}