import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import {
  DataGrid,
} from "@mui/x-data-grid";

export default function MutationTable({ pipeline }) {

  const rows =
    (pipeline?.recommendations || []).map(
      (item,index)=>({

        id:index,

        gene:item.gene,

        drug:item.drug,

        confidence:
          `${(item.confidence*100).toFixed(1)}%`,

        approved:
          item.approved ? "Yes":"No",

      })
    );

  const columns=[

    {
      field:"gene",
      headerName:"Gene",
      flex:1,
    },

    {
      field:"drug",
      headerName:"Drug",
      flex:2,
    },

    {
      field:"confidence",
      headerName:"Confidence",
      flex:1,
    },

    {
      field:"approved",
      headerName:"FDA",
      flex:1,
    },

  ];

  return (

    <Card>

      <CardContent>

        <Typography
          variant="h6"
          gutterBottom
        >

          Mutation Results

        </Typography>

        <DataGrid
          rows={rows}
          columns={columns}
          autoHeight
          disableRowSelectionOnClick
        />

      </CardContent>

    </Card>

  );

}