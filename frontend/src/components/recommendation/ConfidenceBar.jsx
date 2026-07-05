import {
  Box,
  LinearProgress,
  Typography,
} from "@mui/material";

export default function ConfidenceBar({
  confidence,
}) {
  const value = confidence * 100;

  return (
    <Box mt={2}>
      <Typography
        variant="body2"
        gutterBottom
      >
        AI Confidence
      </Typography>

      <LinearProgress
        variant="determinate"
        value={value}
        sx={{
          height: 10,
          borderRadius: 5,
        }}
      />

      <Typography
        mt={1}
        fontWeight="bold"
      >
        {value.toFixed(1)}%
      </Typography>
    </Box>
  );
}