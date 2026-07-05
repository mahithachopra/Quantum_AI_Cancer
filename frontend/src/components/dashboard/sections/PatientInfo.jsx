import {
  Card,
  CardContent,
  Grid,
  Typography,
} from "@mui/material";

export default function PatientInfo({ pipeline }) {
  if (!pipeline) return null;

  return (
    <Card sx={{ mb: 3 }}>
      <CardContent>
        <Typography
          variant="h5"
          fontWeight="bold"
          gutterBottom
        >
          Analysis Summary
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} md={3}>
            <Typography color="text.secondary">
              Genes
            </Typography>

            <Typography variant="h6">
              {pipeline.dashboard?.genes}
            </Typography>
          </Grid>

          <Grid item xs={12} md={3}>
            <Typography color="text.secondary">
              Drugs
            </Typography>

            <Typography variant="h6">
              {pipeline.dashboard?.drugs}
            </Typography>
          </Grid>

          <Grid item xs={12} md={3}>
            <Typography color="text.secondary">
              Processing Time
            </Typography>

            <Typography variant="h6">
              {pipeline.metadata?.processing_time_ms} ms
            </Typography>
          </Grid>

          <Grid item xs={12} md={3}>
            <Typography color="text.secondary">
              Generated
            </Typography>

            <Typography variant="h6">
              {pipeline.metadata?.generated_at?.slice(0,10)}
            </Typography>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}