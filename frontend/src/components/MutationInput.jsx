import { useState } from "react";
import { usePipeline } from "../context/PipelineContext";

import {
  Button,
  Paper,
  TextField,
  Typography,
  CircularProgress,
} from "@mui/material";

import api from "../services/api";

export default function MutationInput({
  setRecommendations,
  setPipelineData,
}) {
  const [genes, setGenes] = useState("");
  const [loading, setLoading] = useState(false);

  const { setPipeline } = usePipeline();

  const analyze = async () => {
    try {
      setLoading(true);

      const response = await api.post("/predict", {
        genes: genes
          .split(",")
          .map((g) => g.trim())
          .filter(Boolean),
      });

      console.log("FULL RESPONSE:", response.data);

      const result = response.data.data;

      console.log("PIPELINE:", result);
      console.log(
        "RECOMMENDATIONS:",
        result?.recommendations
      );

      setRecommendations(
        result?.recommendations || []
      );

      setPipeline(result);

      if (setPipelineData) {
        setPipelineData(result);
      }

    } catch (err) {
      console.error(
        "Prediction Error:",
        err
      );

      if (err.response) {
        console.error(
          "Status:",
          err.response.status
        );
        console.error(
          "Data:",
          err.response.data
        );
      }

      alert("Prediction failed.");

    } finally {
      setLoading(false);
    }
  };

  return (
    <Paper
      elevation={3}
      sx={{
        p: 3,
        borderRadius: 3,
      }}
    >
      <Typography
        variant="h5"
        fontWeight="bold"
        mb={2}
      >
        Mutation Analysis
      </Typography>

      <TextField
        fullWidth
        label="Mutated Genes (comma separated)"
        value={genes}
        onChange={(e) =>
          setGenes(e.target.value)
        }
      />

      <Button
        variant="contained"
        sx={{ mt: 2 }}
        onClick={analyze}
        disabled={loading}
      >
        {loading ? (
          <CircularProgress
            size={24}
            color="inherit"
          />
        ) : (
          "Analyze"
        )}
      </Button>
    </Paper>
  );
}