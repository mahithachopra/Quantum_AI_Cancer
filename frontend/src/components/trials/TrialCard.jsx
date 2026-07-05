import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
  Divider,
  Button,
} from "@mui/material";

export default function TrialCard({ trial }) {

  return (

    <Card
      elevation={3}
      sx={{
        borderRadius:4,
        height:"100%",
        transition:"0.25s",

        "&:hover":{
          transform:"translateY(-4px)",
          boxShadow:8,
        },
      }}
    >

      <CardContent>

        <Typography
          variant="h6"
          fontWeight="bold"
          gutterBottom
        >

          {trial.title}

        </Typography>

        <Stack
          direction="row"
          spacing={1}
          flexWrap="wrap"
          mb={2}
        >

          <Chip
            color="primary"
            label={trial.phase || "Unknown"}
          />

          <Chip
            color={
              (trial.status || "")
                .includes("Recruit")
                ? "success"
                : "default"
            }
            label={trial.status || "Unknown"}
          />

        </Stack>

        <Typography>

          Sponsor

        </Typography>

        <Typography color="text.secondary">

          {trial.sponsor || "Unknown"}

        </Typography>

        <Divider sx={{ my:2 }}/>

        <Typography>

          Enrollment

        </Typography>

        <Typography>

          {trial.enrollment || "N/A"}

        </Typography>

        <Typography mt={2}>

          Condition

        </Typography>

        <Typography color="text.secondary">

          {trial.condition || "Cancer"}

        </Typography>

        <Stack
          direction="row"
          spacing={2}
          mt={3}
        >

          <Button
            variant="contained"
            href={trial.url}
            target="_blank"
            disabled={!trial.url}
          >
            ClinicalTrials.gov
          </Button>

          <Button
            variant="outlined"
          >
            Details
          </Button>

        </Stack>

      </CardContent>

    </Card>

  );

}