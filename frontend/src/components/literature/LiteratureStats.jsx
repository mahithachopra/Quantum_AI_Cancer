import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function LiteratureStats({ papers }) {

  const highest =
    Math.max(...papers.map(p => p.score || 0));

  const genes =
    new Set(papers.map(p => p.gene)).size;

  const drugs =
    new Set(papers.map(p => p.drug)).size;

  const stats = [
    {
      title: "Research Papers",
      value: papers.length,
    },
    {
      title: "Highest Score",
      value: `${(highest * 100).toFixed(1)}%`,
    },
    {
      title: "Genes",
      value: genes,
    },
    {
      title: "Drugs",
      value: drugs,
    },
  ];

  return (
    <Grid
      container
      spacing={3}
      sx={{ mb:4 }}
    >
      {stats.map((item) => (
        <Grid
          key={item.title}
          size={{
            xs:12,
            sm:6,
            md:3,
          }}
        >
          <Card>

            <CardContent>

              <Typography color="text.secondary">

                {item.title}

              </Typography>

              <Typography
                variant="h4"
                fontWeight="bold"
              >
                {item.value}
              </Typography>

            </CardContent>

          </Card>
        </Grid>
      ))}
    </Grid>
  );
}