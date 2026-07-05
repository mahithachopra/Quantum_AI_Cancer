import {
  Card,
  CardContent,
  Typography,
  Stack,
  LinearProgress,
  Chip,
  Divider,
  Box,
} from "@mui/material";

export default function PipelineStatus({ pipeline }) {
  const recommendations = pipeline?.recommendations || [];

  if (!pipeline || recommendations.length === 0) {
    return (
      <Card elevation={3}>
        <CardContent>
          <Typography variant="h6" gutterBottom>
            AI Pipeline Status
          </Typography>

          <Typography color="text.secondary">
            No analysis has been performed yet.
          </Typography>
        </CardContent>
      </Card>
    );
  }

  const avgConfidence =
    recommendations.reduce(
      (sum, item) => sum + Number(item.confidence || 0),
      0
    ) / recommendations.length;

  const geneCount = new Set(
    recommendations.map((r) => r.gene)
  ).size;

  return (
    <Card
      elevation={3}
      sx={{
        borderRadius: 3,
        height: "100%",
      }}
    >
      <CardContent>

        <Typography variant="h6" fontWeight="bold">
          AI Pipeline Status
        </Typography>

        <Typography
          variant="h3"
          color="primary"
          sx={{ mt: 2 }}
        >
          {(avgConfidence * 100).toFixed(1)}%
        </Typography>

        <Typography color="text.secondary">
          Average Recommendation Confidence
        </Typography>

        <LinearProgress
          variant="determinate"
          value={avgConfidence * 100}
          sx={{
            mt: 2,
            height: 10,
            borderRadius: 5,
          }}
        />

        <Divider sx={{ my: 3 }} />

        <Stack spacing={1.5}>

          <Chip
            color="primary"
            label={`Recommendations: ${recommendations.length}`}
          />

          <Chip
            color="success"
            label={`Genes: ${geneCount}`}
          />

          <Chip
            color="warning"
            label={`Clinical Trials: ${
              pipeline.clinical_trials?.length || 0
            }`}
          />

          <Chip
            color="secondary"
            label={`Research Papers: ${
              pipeline.literature?.length || 0
            }`}
          />

        </Stack>

        <Box mt={3}>
          <Typography variant="body2" color="text.secondary">
            Pipeline Version
          </Typography>

          <Typography fontWeight="bold">
            {pipeline.metadata?.pipeline_version || "1.0.0"}
          </Typography>
        </Box>

      </CardContent>
    </Card>
  );
}