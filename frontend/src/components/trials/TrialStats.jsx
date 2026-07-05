import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function TrialStats({ trials }) {

  const recruiting =
    trials.filter(
      t =>
        (t.status || "")
          .toLowerCase()
          .includes("recruit")
    ).length;

  const phase3 =
    trials.filter(
      t =>
        (t.phase || "")
          .includes("III")
    ).length;

  const stats = [
    {
      title: "Trials",
      value: trials.length,
    },
    {
      title: "Recruiting",
      value: recruiting,
    },
    {
      title: "Phase III",
      value: phase3,
    },
    {
      title: "Completed",
      value:
        trials.filter(
          t =>
            (t.status || "")
              .includes("Completed")
        ).length,
    },
  ];

  return (

    <Grid
      container
      spacing={3}
      sx={{ mb:4 }}
    >

      {stats.map(card => (

        <Grid
          key={card.title}
          size={{
            xs:12,
            sm:6,
            md:3,
          }}
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