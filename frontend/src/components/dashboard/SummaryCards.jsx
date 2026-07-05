import Grid from "@mui/material/Grid";
import StatisticsCard from "./StatisticsCard";

import BiotechIcon from "@mui/icons-material/Biotech";
import MedicationIcon from "@mui/icons-material/Medication";
import ScienceIcon from "@mui/icons-material/Science";
import ArticleIcon from "@mui/icons-material/Article";

export default function SummaryCards({ pipeline }) {
  const recommendations = pipeline?.recommendations ?? [];

  const cards = [
    {
      title: "Genes",
      value: new Set(recommendations.map(r => r.gene)).size,
      icon: <BiotechIcon color="primary" fontSize="large" />,
    },
    {
      title: "Drugs",
      value: recommendations.length,
      icon: <MedicationIcon color="success" fontSize="large" />,
    },
    {
      title: "Trials",
      value: pipeline?.clinical_trials?.length ?? 0,
      icon: <ScienceIcon color="warning" fontSize="large" />,
    },
    {
      title: "Papers",
      value: pipeline?.literature?.length ?? 0,
      icon: <ArticleIcon color="secondary" fontSize="large" />,
    },
  ];

  return (
    <Grid container spacing={3} sx={{ mb: 3 }}>
      {cards.map((card) => (
        <Grid
          key={card.title}
          size={{ xs: 12, sm: 6, md: 3 }}
        >
          <StatisticsCard {...card} />
        </Grid>
      ))}
    </Grid>
  );
}