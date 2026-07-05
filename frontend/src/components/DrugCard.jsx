import {
    Card,
    CardContent,
    Typography,
    Chip,
    Stack,
} from "@mui/material";

export default function DrugCard({ drug }) {

    return (

        <Card sx={{ mb: 2 }}>

            <CardContent>

                <Typography variant="h6">
                    {drug.drug}
                </Typography>

                <Typography>
                    Gene: {drug.gene}
                </Typography>

                <Typography>
                    Confidence: {(drug.confidence * 100).toFixed(2)}%
                </Typography>

                <Stack direction="row" spacing={1} mt={2}>

                    <Chip
                        label={drug.gene}
                        color="primary"
                    />

                </Stack>

            </CardContent>

        </Card>

    );

}