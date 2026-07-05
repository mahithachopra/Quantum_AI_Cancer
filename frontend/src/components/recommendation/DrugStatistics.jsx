import {
  Grid,
  Paper,
  Typography,
} from "@mui/material";

export default function DrugStatistics({
  drug,
}) {
  return (
    <Grid
      container
      spacing={2}
      mt={1}
    >
      <Grid item xs={4}>
        <Paper sx={{ p: 2 }}>
          <Typography variant="body2">
            Evidence
          </Typography>

          <Typography variant="h6">
            {drug.evidence?.length ?? 0}
          </Typography>
        </Paper>
      </Grid>

      <Grid item xs={4}>
        <Paper sx={{ p: 2 }}>
          <Typography variant="body2">
            Trials
          </Typography>

          <Typography variant="h6">
            {drug.trials ?? 0}
          </Typography>
        </Paper>
      </Grid>

      <Grid item xs={4}>
        <Paper sx={{ p: 2 }}>
          <Typography variant="body2">
            Papers
          </Typography>

          <Typography variant="h6">
            {drug.papers ?? 0}
          </Typography>
        </Paper>
      </Grid>
    </Grid>
  );
}