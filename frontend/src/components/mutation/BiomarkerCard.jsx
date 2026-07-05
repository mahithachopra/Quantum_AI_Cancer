import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
} from "@mui/material";

export default function BiomarkerCard({ pipeline }) {

  const approved =
    (pipeline?.recommendations || [])
      .filter(r=>r.approved);

  return (

    <Card sx={{mb:3}}>

      <CardContent>

        <Typography
          variant="h6"
          gutterBottom
        >

          Biomarkers

        </Typography>

        <Stack spacing={2}>

          {approved.length===0 ? (

            <Typography>

              No FDA approved biomarkers

            </Typography>

          ):approved.map((item,index)=>(

            <Chip
              key={index}
              color="success"
              label={item.gene}
            />

          ))}

        </Stack>

      </CardContent>

    </Card>

  );

}