import { useState } from "react";

import {
  Grid,
  Box,
} from "@mui/material";

import SummaryCards from "../components/dashboard/SummaryCards";
import PatientSummary from "../components/dashboard/PatientSummary";
import SearchBar from "../components/dashboard/SearchBar";
import MutationInput from "../components/MutationInput";
import RecommendationTable from "../components/RecommendationTable";
import ConfidenceChart from "../components/dashboard/ConfidenceChart";
import PipelineStatus from "../components/dashboard/PipelineStatus";
import PatientInfo from "../components/dashboard/sections/PatientInfo";

export default function Home() {
  const [recommendations, setRecommendations] = useState([]);
  const [pipelineData, setPipelineData] = useState(null);

  return (
    <>
      <SummaryCards pipeline={pipelineData} />
      <PatientInfo pipeline={pipelineData} />


      <PatientSummary pipeline={pipelineData} />

      <SearchBar />

      <Box mt={3}>
        <MutationInput
          setRecommendations={setRecommendations}
          setPipelineData={setPipelineData}
        />
      </Box>

      <Grid
  container
  spacing={3}
  sx={{ mt: 2 }}
>
  <Grid size={{ xs: 12, md: 8 }}>
    <ConfidenceChart
      recommendations={recommendations}
    />
  </Grid>

  <Grid size={{ xs: 12, md: 4 }}>
    <PipelineStatus
      pipeline={pipelineData}
    />
  </Grid>
</Grid>

      {/* Temporary Debug Panel */}
      

      <Box mt={4}>
        <RecommendationTable
          recommendations={recommendations}
          pipeline={pipelineData}
        />
      </Box>
    </>
  );
}