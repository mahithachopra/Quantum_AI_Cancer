import {
  Paper,
  Grid,
  TextField,
  MenuItem,
} from "@mui/material";

export default function RecommendationToolbar() {
  return (
    <Paper
      sx={{
        p: 2,
        mb: 3,
      }}
    >
      <Grid
        container
        spacing={2}
      >

        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Search Drug"
          />
        </Grid>

        <Grid item xs={12} md={3}>
          <TextField
            fullWidth
            select
            label="Confidence"
            defaultValue=""
          >
            <MenuItem value="">
              All
            </MenuItem>

            <MenuItem value="0.6">
              Above 60%
            </MenuItem>

            <MenuItem value="0.7">
              Above 70%
            </MenuItem>

            <MenuItem value="0.8">
              Above 80%
            </MenuItem>

          </TextField>
        </Grid>

        <Grid item xs={12} md={3}>
          <TextField
            fullWidth
            select
            label="Sort"
            defaultValue=""
          >
            <MenuItem value="">
              Default
            </MenuItem>

            <MenuItem value="confidence">
              Confidence
            </MenuItem>

            <MenuItem value="drug">
              Drug Name
            </MenuItem>

          </TextField>
        </Grid>

      </Grid>
    </Paper>
  );
}