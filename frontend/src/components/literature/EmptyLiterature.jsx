import {
  Alert,
  Box,
} from "@mui/material";

export default function EmptyLiterature() {
  return (
    <Box mt={5}>
      <Alert severity="info">
        No literature available.

        Run mutation analysis first.
      </Alert>
    </Box>
  );
}