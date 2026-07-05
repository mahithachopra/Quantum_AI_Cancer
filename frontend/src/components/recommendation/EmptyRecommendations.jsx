import { Alert } from "@mui/material";

export default function EmptyRecommendations() {
  return (
    <Alert severity="info" sx={{ mt: 2 }}>
      Run a mutation analysis to generate AI drug recommendations.
    </Alert>
  );
}