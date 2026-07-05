import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

import { Card, CardContent, Typography } from "@mui/material";

export default function ConfidenceChart({ recommendations }) {
  if (!recommendations.length) return null;

  const data = recommendations.map((r) => ({
    drug: r.drug,
    confidence: Number((r.confidence * 100).toFixed(1)),
  }));

  return (
    <Card elevation={3}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Recommendation Confidence
        </Typography>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
              dataKey="drug"
              angle={-30}
              textAnchor="end"
              interval={0}
              height={90}
            />

            <YAxis domain={[0, 100]} />

            <Tooltip />

            <Bar
              dataKey="confidence"
              radius={[5, 5, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}