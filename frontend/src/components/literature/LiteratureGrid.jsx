import { Grid } from "@mui/material";

import LiteratureCard from "./LiteratureCard";

export default function LiteratureGrid({ papers }) {

  return (

    <Grid container spacing={3}>

      {papers.map((paper,index)=>(

        <Grid
          key={index}
          size={{
            xs:12,
            lg:6,
          }}
        >

          <LiteratureCard
            paper={paper}
          />

        </Grid>

      ))}

    </Grid>

  );

}