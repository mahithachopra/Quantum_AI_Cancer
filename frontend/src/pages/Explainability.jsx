import { Container, Grid, Typography } from "@mui/material";
import { usePipeline } from "../context/PipelineContext";

import ExplainabilityDashboard from "../components/explainability/ExplainabilityDashboard";
import AIReasoningCard from "../components/explainability/AIReasoningCard";
import ConfidenceBreakdown from "../components/explainability/ConfidenceBreakdown";
import DecisionTree from "../components/explainability/DecisionTree";
import EvidenceScoreCard from "../components/explainability/EvidenceScoreCard";
import LiteratureEvidence from "../components/explainability/LiteratureEvidence";
import TrialEvidence from "../components/explainability/TrialEvidence";

export default function Explainability() {

    const { pipeline } = usePipeline();

    if (!pipeline) {
        return (
            <Container maxWidth="lg">
                <Typography variant="h4">
                    Run a mutation analysis first.
                </Typography>
            </Container>
        );
    }

    return (

        <Container maxWidth="xl">

            <Typography
                variant="h3"
                fontWeight="bold"
                mb={3}
            >
                Explainable AI
            </Typography>

            <ExplainabilityDashboard pipeline={pipeline} />

            <Grid container spacing={3} mt={1}>

                <Grid size={{ xs:12, md:6 }}>
                    <AIReasoningCard pipeline={pipeline}/>
                </Grid>

                <Grid size={{ xs:12, md:6 }}>
                    <ConfidenceBreakdown pipeline={pipeline}/>
                </Grid>

                <Grid size={{ xs:12, md:6 }}>
                    <DecisionTree/>
                </Grid>

                <Grid size={{ xs:12, md:6 }}>
                    <EvidenceScoreCard pipeline={pipeline}/>
                </Grid>

                <Grid size={{ xs:12, md:6 }}>
                    <LiteratureEvidence pipeline={pipeline}/>
                </Grid>

                <Grid size={{ xs:12, md:6 }}>
                    <TrialEvidence pipeline={pipeline}/>
                </Grid>

            </Grid>

        </Container>

    );

}