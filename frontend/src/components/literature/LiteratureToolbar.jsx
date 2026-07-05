import { useState } from "react";

import {
  Paper,
  Grid,
  TextField,
  MenuItem,
} from "@mui/material";

export default function LiteratureToolbar() {

  const [year, setYear] = useState("");

  const [sort, setSort] = useState("");

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
            label="Search Title / Drug / Gene"
          />

        </Grid>

        <Grid size={{ xs:12, md:3 }}>

          <TextField
            fullWidth
            select
            label="Year"
            value={year}
            onChange={(e)=>setYear(e.target.value)}
          >

            <MenuItem value="">
              Any
            </MenuItem>

            <MenuItem value="2026">
              2026
            </MenuItem>

          </TextField>

        </Grid>

        <Grid size={{ xs:12, md:3 }}>

          <TextField
            fullWidth
            select
            label="Sort"
            value={sort}
            onChange={(e)=>setSort(e.target.value)}
          >

            <MenuItem value="">
              Default
            </MenuItem>

            <MenuItem value="score">
              Highest Score
            </MenuItem>

            <MenuItem value="year">
              Newest
            </MenuItem>

          </TextField>

        </Grid>

      </Grid>

    </Paper>

  );

}