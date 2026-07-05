import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
} from "@mui/material";

export default function PathwayCard({ pipeline }) {

  const pathways =
    pipeline?.pathway_analysis || [];

  return (

    <Card sx={{mb:3}}>

      <CardContent>

        <Typography
          variant="h6"
          gutterBottom
        >

          Cancer Pathways

        </Typography>

        <Stack
          direction="row"
          spacing={1}
          flexWrap="wrap"
        >

          {pathways.map((p,index)=>(

            <Chip
              key={index}
              label={
                p.name ||
                p.pathway ||
                p
              }
            />

          ))}

        </Stack>

      </CardContent>

    </Card>

  );

}