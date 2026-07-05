import { Typography, Box } from "@mui/material";

export default function ReportHeader() {

    return(

        <Box mb={3}>

            <Typography variant="h3" fontWeight="bold">

                Clinical AI Report

            </Typography>

            <Typography color="text.secondary">

                Precision Oncology Decision Support

            </Typography>

        </Box>

    )

}