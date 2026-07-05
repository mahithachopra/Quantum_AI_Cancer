import { Stack, Chip } from "@mui/material";

export default function DrugBadges() {
  return (
    <Stack
      direction="row"
      spacing={1}
      mt={2}
      flexWrap="wrap"
    >
      <Chip
        label="Targeted Therapy"
        color="primary"
      />

      <Chip
        label="FDA Approved"
        color="success"
      />

      <Chip
        label="AI Recommended"
        color="secondary"
      />
    </Stack>
  );
}