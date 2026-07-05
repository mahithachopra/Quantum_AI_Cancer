import {
  Card,
  CardContent,
  Grid,
  Typography,
  Chip,
  Stack,
} from "@mui/material";

export default function PatientSummary({ pipeline }) {
  if (!pipeline) return null;

  const mutation = pipeline.mutation_analysis;

  return (
    <Card
      elevation={3}
      sx={{ mb: 3 }}
    >
      <CardContent>

        <Typography
          variant="h5"
          gutterBottom
        >
          Patient Summary
        </Typography>

        <Grid
          container
          spacing={3}
        >
          <Grid size={{ xs: 12, md: 4 }}>

            <Typography fontWeight="bold">
              Mutated Genes
            </Typography>

            <Stack
              direction="row"
              spacing={1}
              sx={{
                mt: 1,
                flexWrap: "wrap",
                gap: 1,
              }}
            >
              {(mutation?.genes || []).map((gene) => (
                <Chip
                  key={gene}
                  label={gene}
                />
              ))}
            </Stack>

          </Grid>

          <Grid size={{ xs: 12, md: 4 }}>

            <Typography fontWeight="bold">
              Pathways
            </Typography>

            <Typography>
              {pipeline.pathway_analysis?.length ?? 0}
            </Typography>

          </Grid>

          <Grid size={{ xs: 12, md: 4 }}>

            <Typography fontWeight="bold">
              Clinical Evidence
            </Typography>

            <Typography>
              {pipeline.clinical_evidence?.length ?? 0}
            </Typography>

          </Grid>

        </Grid>

      </CardContent>
    </Card>
  );
}