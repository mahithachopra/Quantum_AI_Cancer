import {
  Box,
  Typography,
  Chip,
} from "@mui/material";

export default function DrugHeader({ drug }) {
  const confidence =
    Math.round(drug.confidence * 100);

  let color = "error";

  if (confidence >= 80) color = "success";
  else if (confidence >= 60) color = "warning";

  return (
    <Box
      display="flex"
      justifyContent="space-between"
      alignItems="center"
    >
      <Box>
        <Typography
          variant="h5"
          fontWeight="bold"
        >
          {drug.drug}
        </Typography>

        <Typography color="text.secondary">
          Target Gene: {drug.gene}
        </Typography>
      </Box>

      <Chip
        label={`${confidence}%`}
        color={color}
      />
    </Box>
  );
}