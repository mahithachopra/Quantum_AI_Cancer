import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
  Button,
  LinearProgress,
} from "@mui/material";

export default function RecommendationCard({
  drug,
}) {
  return (
    <Card
      elevation={3}
      sx={{
        borderRadius: 3,
        height: "100%",
      }}
    >
      <CardContent>

        <Typography
          variant="h5"
          fontWeight="bold"
        >
          {drug.drug}
        </Typography>

        <Typography
          color="text.secondary"
          mb={2}
        >
          Target Gene: {drug.gene}
        </Typography>

        <Typography
          gutterBottom
        >
          AI Confidence
        </Typography>

        <LinearProgress
          variant="determinate"
          value={drug.confidence * 100}
          sx={{
            height: 10,
            borderRadius: 5,
            mb: 1,
          }}
        />

        <Typography
          mb={2}
        >
          {(drug.confidence * 100).toFixed(1)}%
        </Typography>

        <Stack
          direction="row"
          spacing={1}
          flexWrap="wrap"
          mb={2}
        >

          <Chip
            label={`Gene: ${drug.gene}`}
            color="primary"
          />

          <Chip
            label={
              drug.approved
                ? "FDA Approved"
                : "Research"
            }
            color={
              drug.approved
                ? "success"
                : "warning"
            }
          />

          <Chip
            label={`Score ${(
              drug.final_score * 100
            ).toFixed(1)}%`}
            color="info"
          />

        </Stack>

        <Typography
          variant="body2"
          color="text.secondary"
        >
          Drug Class
        </Typography>

        <Typography mb={2}>
          {drug.drug_class || "Unknown"}
        </Typography>

        <Typography
          variant="body2"
          color="text.secondary"
        >
          Mechanism
        </Typography>

        <Typography mb={3}>
          {drug.mechanism || "Not Available"}
        </Typography>

        <Button
          fullWidth
          variant="contained"
        >
          View Details
        </Button>

      </CardContent>
    </Card>
  );
}