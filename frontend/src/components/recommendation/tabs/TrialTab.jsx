import {
    Card,
    CardContent,
    Typography
} from "@mui/material";

export default function TrialTab({ drug }) {

    const trials = drug.evidence?.top_trials || [];

    if (!trials.length)

        return (

            <Typography>

                No clinical trials.

            </Typography>

        );

    return (

        <>

            {

                trials.map(

                    (trial, index) => (

                        <Card
                            key={index}
                            sx={{ mb: 2 }}
                        >

                            <CardContent>

                                <Typography>

                                    {trial.nct_id}

                                </Typography>

                                <Typography>

                                    {trial.phase}

                                </Typography>

                                <Typography>

                                    {trial.status}

                                </Typography>

                            </CardContent>

                        </Card>

                    )

                )

            }

        </>

    );

}