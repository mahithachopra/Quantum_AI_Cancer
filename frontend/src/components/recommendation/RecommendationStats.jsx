import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function RecommendationStats({
  recommendations,
}) {
  const avg =
    recommendations.length === 0
      ? 0
      : recommendations.reduce(
          (sum, r) => sum + Number(r.confidence),
          0
        ) / recommendations.length;

  const approved =
    recommendations.filter(
      (r) => r.approved
    ).length;

  const cards = [
    {
      title: "Recommendations",
      value: recommendations.length,
    },
    {
      title: "Average Confidence",
      value: `${(avg * 100).toFixed(1)}%`,
    },
    {
      title: "FDA Approved",
      value: approved,
    },
  ];

  return (
    <Grid
      container
      spacing={2}
      sx={{ mb: 3 }}
    >
      {cards.map((card) => (
        <Grid
          item
          xs={12}
          md={4}
          key={card.title}
        >
          <Card>

            <CardContent>

              <Typography
                color="text.secondary"
              >
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