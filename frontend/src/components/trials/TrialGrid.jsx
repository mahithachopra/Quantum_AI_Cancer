import { Grid } from "@mui/material";

import TrialCard from "./TrialCard";

export default function TrialGrid({ trials }) {

  return (

    <Grid container spacing={3}>

      {trials.map((trial,index)=>(

        <Grid
          key={index}
          size={{
            xs:12,
            lg:6,
          }}
        >

          <TrialCard
            trial={trial}
          />

        </Grid>

      ))}

    </Grid>

  );

}