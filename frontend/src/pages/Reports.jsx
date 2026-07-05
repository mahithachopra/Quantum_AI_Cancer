import { useRef } from "react";

import { Box, Grid } from "@mui/material";
import { usePipeline } from "../context/PipelineContext";

import ReportHeader from "../components/reports/ReportHeader";
import PatientInfoCard from "../components/reports/PatientInfoCard";
import ExecutiveSummary from "../components/reports/ExecutiveSummary";
import DrugReportTable from "../components/reports/DrugReportTable";
import LiteratureSection from "../components/reports/LiteratureSection";
import TrialSection from "../components/reports/TrialSection";
import ExportButtons from "../components/reports/ExportButtons";
import ReportFooter from "../components/reports/ReportFooter";

export default function Reports() {
  const { pipeline } = usePipeline();

  const reportRef = useRef(null);

  if (!pipeline) {
    return (
      <Box p={4}>
        Run a mutation analysis first.
      </Box>
    );
  }

  return (
    <Box
      ref={reportRef}
      id="clinical-report"
      sx={{ pb: 4 }}
    >
      <ReportHeader pipeline={pipeline} />

      <Grid container spacing={3} sx={{ mt: 1 }}>

        <Grid size={{ xs: 12 }}>
          <PatientInfoCard pipeline={pipeline} />
        </Grid>

        <Grid size={{ xs: 12 }}>
          <ExecutiveSummary pipeline={pipeline} />
        </Grid>

        <Grid size={{ xs: 12 }}>
          <DrugReportTable pipeline={pipeline} />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <LiteratureSection pipeline={pipeline} />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <TrialSection pipeline={pipeline} />
        </Grid>

        <Grid size={{ xs: 12 }}>
          <ExportButtons
            pipeline={pipeline}
            reportRef={reportRef}
          />
        </Grid>

      </Grid>

      <ReportFooter pipeline={pipeline} />
    </Box>
  );
}