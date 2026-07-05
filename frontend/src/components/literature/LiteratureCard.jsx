import {
  Card,
  CardContent,
  Typography,
  Stack,
  Chip,
  Button,
  LinearProgress,
} from "@mui/material";

export default function LiteratureCard({ paper }) {

  const score =
    Number((paper.score || 0) * 100);

  return (

    <Card
      elevation={3}
      sx={{
        height:"100%",
        borderRadius:3,
      }}
    >

      <CardContent>

        <Typography
          variant="h6"
          fontWeight="bold"
          gutterBottom
        >
          {paper.title}
        </Typography>

        <Typography color="text.secondary">

          {paper.journal}

          {" • "}

          {paper.year}

        </Typography>

        <Stack
          direction="row"
          spacing={1}
          mt={2}
          mb={2}
          flexWrap="wrap"
        >

          <Chip
            color="primary"
            label={paper.gene}
          />

          <Chip
            color="success"
            label={paper.drug}
          />

        </Stack>

        <Typography>

          Relevance

        </Typography>

        <LinearProgress
          variant="determinate"
          value={score}
          sx={{
            my:1,
            height:8,
            borderRadius:4,
          }}
        />

        <Typography mb={2}>

          {score.toFixed(1)}%

        </Typography>

        <Typography
          variant="body2"
          color="text.secondary"
          sx={{
            minHeight:90,
          }}
        >
          {paper.summary}
        </Typography>

        <Stack
          direction="row"
          spacing={1}
          mt={3}
        >

          <Button
            variant="contained"
            disabled={!paper.url}
            href={paper.url}
            target="_blank"
          >
            PubMed
          </Button>

          <Button
            variant="outlined"
            disabled={!paper.doi}
            href={
              paper.doi
                ? `https://doi.org/${paper.doi}`
                : undefined
            }
            target="_blank"
          >
            DOI
          </Button>

        </Stack>

      </CardContent>

    </Card>

  );

}