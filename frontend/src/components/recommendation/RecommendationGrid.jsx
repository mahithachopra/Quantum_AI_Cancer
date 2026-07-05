import {
  Grid,
} from "@mui/material";

import RecommendationCard from "./RecommendationCard";

export default function RecommendationGrid({
  recommendations,
}) {
  return (
    <Grid
      container
      spacing={3}
    >
      {recommendations.map((drug, index) => (
        <Grid
          item
          xs={12}
          md={6}
          lg={4}
          key={index}
        >
          <RecommendationCard
            drug={drug}
          />
        </Grid>
      ))}
    </Grid>
  );
}