import { Grid } from "@mui/material";
import StatisticsCard from "../dashboard/StatisticsCard";

import PsychologyIcon from "@mui/icons-material/Psychology";
import ScienceIcon from "@mui/icons-material/Science";
import ArticleIcon from "@mui/icons-material/Article";
import VaccinesIcon from "@mui/icons-material/Vaccines";

export default function ExplainabilityDashboard({ pipeline }) {

  const recommendations = pipeline?.recommendations || [];

  const avg =
    recommendations.length
      ? recommendations.reduce(
          (s, r) => s + Number(r.confidence || 0),
          0
        ) / recommendations.length
      : 0;

  const cards = [
    {
      title: "AI Confidence",
      value: `${(avg * 100).toFixed(1)}%`,
      icon: <PsychologyIcon color="primary" fontSize="large" />,
    },
    {
      title: "Evidence",
      value: pipeline?.clinical_evidence?.length || 0,
      icon: <ScienceIcon color="success" fontSize="large" />,
    },
    {
      title: "Literature",
      value: pipeline?.literature?.length || 0,
      icon: <ArticleIcon color="warning" fontSize="large" />,
    },
    {
      title: "Trials",
      value: pipeline?.clinical_trials?.length || 0,
      icon: <VaccinesIcon color="secondary" fontSize="large" />,
    },
  ];

  return (
    <Grid container spacing={3}>
      {cards.map((card) => (
        <Grid key={card.title} size={{ xs:12, sm:6, md:3 }}>
          <StatisticsCard {...card}/>
        </Grid>
      ))}
    </Grid>
  );
}