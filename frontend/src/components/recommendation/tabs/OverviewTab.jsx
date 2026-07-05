import {
    Grid,
    Typography,
    LinearProgress,
    Chip,
    Stack
} from "@mui/material";

export default function OverviewTab({ drug }) {

    return (

        <Grid container spacing={2}>

            <Grid item xs={12}>

                <Typography variant="h6">

                    {drug.drug}

                </Typography>

                <Typography color="text.secondary">

                    Target Gene : {drug.gene}

                </Typography>

            </Grid>

            <Grid item xs={12}>

                <Typography gutterBottom>

                    Confidence

                </Typography>

                <LinearProgress
                    variant="determinate"
                    value={(drug.confidence || 0) * 100}
                    sx={{
                        height: 12,
                        borderRadius: 6
                    }}
                />

                <Typography mt={1}>

                    {((drug.confidence || 0) * 100).toFixed(2)}%

                </Typography>

            </Grid>

            <Grid item xs={12}>

                <Stack
                    direction="row"
                    spacing={1}
                    flexWrap="wrap"
                >

                    <Chip
                        label={`AI ${drug.ai_score ?? 0}`}
                        color="primary"
                    />

                    <Chip
                        label={`Evidence ${drug.civic_score ?? 0}`}
                        color="success"
                    />

                    <Chip
                        label={`Literature ${drug.literature_score ?? 0}`}
                        color="secondary"
                    />

                    <Chip
                        label={`Trials ${drug.trial_score ?? 0}`}
                        color="warning"
                    />

                </Stack>

            </Grid>

            <Grid item xs={12}>

                <Typography variant="subtitle1">

                    AI Reasoning

                </Typography>

                {

                    (drug.reasoning || []).map(

                        (reason, index) => (

                            <Typography key={index}>

                                • {reason}

                            </Typography>

                        )

                    )

                }

            </Grid>

        </Grid>

    );

}