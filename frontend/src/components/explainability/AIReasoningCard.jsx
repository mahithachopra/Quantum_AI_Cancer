import {
  Card,
  CardContent,
  Typography,
  List,
  ListItem,
  ListItemIcon,
} from "@mui/material";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";

export default function AIReasoningCard({ pipeline }) {

  const gene =
    pipeline?.recommendations?.[0]?.gene || "Unknown";

  return (
    <Card>

      <CardContent>

        <Typography
          variant="h5"
          gutterBottom
        >
          AI Reasoning
        </Typography>

        <List>

          <ListItem>

            <ListItemIcon>

              <CheckCircleIcon color="success"/>

            </ListItemIcon>

            EGFR mutation detected

          </ListItem>

          <ListItem>

            <ListItemIcon>

              <CheckCircleIcon color="success"/>

            </ListItemIcon>

            Targeted therapies available

          </ListItem>

          <ListItem>

            <ListItemIcon>

              <CheckCircleIcon color="success"/>

            </ListItemIcon>

            Clinical evidence identified

          </ListItem>

          <ListItem>

            <ListItemIcon>

              <CheckCircleIcon color="success"/>

            </ListItemIcon>

            Literature supports recommendation

          </ListItem>

          <ListItem>

            <ListItemIcon>

              <CheckCircleIcon color="success"/>

            </ListItemIcon>

            Recommended for gene {gene}

          </ListItem>

        </List>

      </CardContent>

    </Card>
  );

}