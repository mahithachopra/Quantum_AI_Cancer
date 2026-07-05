import { Container, Typography } from "@mui/material";
import { usePipeline } from "../context/PipelineContext";

import LiteratureToolbar from "../components/literature/LiteratureToolbar";
import LiteratureStats from "../components/literature/LiteratureStats";
import LiteratureGrid from "../components/literature/LiteratureGrid";
import EmptyLiterature from "../components/literature/EmptyLiterature";

export default function Literature() {
  const { pipeline } = usePipeline();

  const papers = pipeline?.literature || [];

  return (
    <Container maxWidth="xl">

      <Typography
        variant="h3"
        fontWeight="bold"
        mb={3}
      >
        Literature
      </Typography>

      {!papers.length ? (
        <EmptyLiterature />
      ) : (
        <>
          <LiteratureToolbar />

          <LiteratureStats papers={papers} />

          <LiteratureGrid papers={papers} />
        </>
      )}

    </Container>
  );
}