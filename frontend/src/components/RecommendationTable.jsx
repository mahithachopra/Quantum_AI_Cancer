import {
  Box,
  Typography,
  Alert,
} from "@mui/material";

import RecommendationCard from "./recommendations/RecommendationCard";

export default function RecommendationTable({
  recommendations = [],
}) {
  console.log("RecommendationTable");
  console.log(recommendations);

  if (recommendations.length === 0) {
    return (
      <Alert severity="info" sx={{ mt: 4 }}>
        No recommendations available.
      </Alert>
    );
  }

  return (
    <Box sx={{ mt: 4 }}>
      <Typography
        variant="h4"
        fontWeight="bold"
        gutterBottom
      >
        Drug Recommendations
      </Typography>

      <Typography
        variant="body1"
        color="text.secondary"
        sx={{ mb: 3 }}
      >
        {recommendations.length} recommendation(s) generated
      </Typography>

      {recommendations.map((drug, index) => (
        <RecommendationCard
          key={`${drug.gene}-${drug.drug}-${index}`}
          drug={drug}
        />
      ))}
    </Box>
  );
}