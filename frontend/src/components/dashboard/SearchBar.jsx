import { useState } from "react";

import {
  Paper,
  TextField,
  MenuItem,
  Grid,
} from "@mui/material";

export default function SearchBar() {
  const [confidence, setConfidence] = useState("");
  const [sort, setSort] = useState("");

  return (
    <Paper
      elevation={2}
      sx={{
        p: 3,
        mt: 3,
      }}
    >
      <Grid
        container
        spacing={2}
      >

        <Grid size={{ xs: 12, md: 4 }}>

          <TextField
            fullWidth
            label="Search Drug"
          />

        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>

          <TextField
            fullWidth
            select
            label="Minimum Confidence"
            value={confidence}
            onChange={(e) =>
              setConfidence(e.target.value)
            }
          >
            <MenuItem value="">
              Any
            </MenuItem>

            <MenuItem value={0.5}>
              50%
            </MenuItem>

            <MenuItem value={0.6}>
              60%
            </MenuItem>

            <MenuItem value={0.7}>
              70%
            </MenuItem>

            <MenuItem value={0.8}>
              80%
            </MenuItem>

          </TextField>

        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>

          <TextField
            fullWidth
            select
            label="Sort"
            value={sort}
            onChange={(e) =>
              setSort(e.target.value)
            }
          >
            <MenuItem value="">
              Default
            </MenuItem>

            <MenuItem value="confidence">
              Confidence
            </MenuItem>

            <MenuItem value="evidence">
              Evidence
            </MenuItem>

            <MenuItem value="trials">
              Clinical Trials
            </MenuItem>

          </TextField>

        </Grid>

      </Grid>
    </Paper>
  );
}