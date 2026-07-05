import { usePipeline } from "../context/PipelineContext";
import {
  Typography,
  Box,
} from "@mui/material";

import RecommendationToolbar from "../components/recommendations/RecommendationToolbar";

import RecommendationStats from "../components/recommendations/RecommendationStats";

import RecommendationGrid from "../components/recommendations/RecommendationGrid";

import EmptyRecommendations from "../components/recommendations/EmptyRecommendations";

export default function Recommendations() {
  const { pipeline } = usePipeline();

  const recommendations =
    pipeline?.recommendations || [];

  return (
    <Box>

      <Typography
        variant="h4"
        fontWeight="bold"
        mb={3}
      >
        AI Drug Recommendations
      </Typography>

      <RecommendationToolbar />

      <RecommendationStats
        recommendations={recommendations}
      />

      {recommendations.length === 0 ? (
        <EmptyRecommendations />
      ) : (
        <RecommendationGrid
          recommendations={recommendations}
        />
      )}

    </Box>
  );
}