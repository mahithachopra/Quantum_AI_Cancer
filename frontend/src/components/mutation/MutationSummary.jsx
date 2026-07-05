import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function MutationSummary({ pipeline }) {

  const recommendations = pipeline?.recommendations || [];

  const confidence =
    recommendations.length
      ? recommendations.reduce(
          (a,b)=>a+Number(b.confidence),
          0
        )/recommendations.length
      : 0;

  const cards = [

    {
      title:"Genes",
      value:new Set(
        recommendations.map(r=>r.gene)
      ).size,
    },

    {
      title:"Pathways",
      value:pipeline?.pathway_analysis?.length || 0,
    },

    {
      title:"Evidence",
      value:pipeline?.literature?.length || 0,
    },

    {
      title:"Confidence",
      value:`${(confidence*100).toFixed(1)}%`,
    },

  ];

  return (

    <Grid
      container
      spacing={3}
      sx={{my:3}}
    >

      {cards.map(card=>(

        <Grid
          key={card.title}
          size={{xs:12,sm:6,md:3}}
        >

          <Card>

            <CardContent>

              <Typography color="text.secondary">

                {card.title}

              </Typography>

              <Typography
                variant="h4"
                fontWeight="bold"
              >

                {card.value}

              </Typography>

            </CardContent>

          </Card>

        </Grid>

      ))}

    </Grid>

  );

}