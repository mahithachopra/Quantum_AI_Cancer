import { useState } from "react";

import {
  Paper,
  Grid,
  TextField,
  MenuItem,
} from "@mui/material";

export default function TrialToolbar() {

  const [phase, setPhase] = useState("");

  const [status, setStatus] = useState("");

  return (

    <Paper
      sx={{
        p:3,
        mb:3,
      }}
    >

      <Grid container spacing={2}>

        <Grid size={{ xs:12, md:6 }}>

          <TextField
            fullWidth
            label="Search Trial"
          />

        </Grid>

        <Grid size={{ xs:12, md:3 }}>

          <TextField
            fullWidth
            select
            label="Phase"
            value={phase}
            onChange={(e)=>setPhase(e.target.value)}
          >

            <MenuItem value="">
              Any
            </MenuItem>

            <MenuItem value="I">
              Phase I
            </MenuItem>

            <MenuItem value="II">
              Phase II
            </MenuItem>

            <MenuItem value="III">
              Phase III
            </MenuItem>

          </TextField>

        </Grid>

        <Grid size={{ xs:12, md:3 }}>

          <TextField
            fullWidth
            select
            label="Status"
            value={status}
            onChange={(e)=>setStatus(e.target.value)}
          >

            <MenuItem value="">
              Any
            </MenuItem>

            <MenuItem value="Recruiting">
              Recruiting
            </MenuItem>

            <MenuItem value="Completed">
              Completed
            </MenuItem>

          </TextField>

        </Grid>

      </Grid>

    </Paper>

  );

}