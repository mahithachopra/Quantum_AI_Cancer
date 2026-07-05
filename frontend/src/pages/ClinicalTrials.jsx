import { Container, Typography } from "@mui/material";
import { usePipeline } from "../context/PipelineContext";

import TrialToolbar from "../components/trials/TrialToolbar";
import TrialStats from "../components/trials/TrialStats";
import TrialGrid from "../components/trials/TrialGrid";
import EmptyTrials from "../components/trials/EmptyTrials";

export default function ClinicalTrials() {

  const { pipeline } = usePipeline();

  const trials = pipeline?.clinical_trials || [];

  return (
    <Container maxWidth="xl">

      <Typography
        variant="h3"
        fontWeight="bold"
        mb={3}
      >
        Clinical Trials
      </Typography>

      {!trials.length ? (
        <EmptyTrials />
      ) : (
        <>
          <TrialToolbar />
          <TrialStats trials={trials} />
          <TrialGrid trials={trials} />
        </>
      )}

    </Container>
  );
}