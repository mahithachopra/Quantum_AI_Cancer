import { Container, Typography, Grid } from "@mui/material";
import { usePipeline } from "../context/PipelineContext";

import GeneInputCard from "../components/mutation/GeneInputCard";
import MutationSummary from "../components/mutation/MutationSummary";
import MutationTable from "../components/mutation/MutationTable";
import PathwayCard from "../components/mutation/PathwayCard";
import BiomarkerCard from "../components/mutation/BiomarkerCard";
import PipelineTimeline from "../components/mutation/PipelineTimeline";

export default function MutationAnalysis() {

  const { pipeline } = usePipeline();

  return (
    <Container maxWidth="xl">

      <Typography
        variant="h3"
        fontWeight="bold"
        mb={3}
      >
        Mutation Analysis
      </Typography>

      <GeneInputCard />

      {pipeline && (
        <>
          <MutationSummary pipeline={pipeline} />

          <Grid container spacing={3}>

            <Grid size={{ xs:12, lg:8 }}>
              <MutationTable pipeline={pipeline} />
            </Grid>

            <Grid size={{ xs:12, lg:4 }}>
              <PathwayCard pipeline={pipeline} />

              <BiomarkerCard pipeline={pipeline} />

              <PipelineTimeline />
            </Grid>

          </Grid>

        </>
      )}

    </Container>
  );
}