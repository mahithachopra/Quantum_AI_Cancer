import { Alert, Box } from "@mui/material";

export default function EmptyTrials() {

  return (

    <Box mt={5}>

      <Alert severity="info">

        No clinical trials available.

        Run mutation analysis first.

      </Alert>

    </Box>

  );

}