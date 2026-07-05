import {
    Typography,
    Stack,
    Chip
} from "@mui/material";

export default function MechanismTab({ drug }) {

    return (

        <>

            <Typography variant="h6">

                Drug Mechanism

            </Typography>

            <Typography mt={2}>

                {drug.mechanism || "Not available"}

            </Typography>

            <Stack
                direction="row"
                spacing={1}
                mt={3}
            >

                <Chip
                    label={
                        drug.drug_class ||
                        "Unknown Class"
                    }
                />

            </Stack>

        </>

    );

}