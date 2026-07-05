import {
  Card,
  CardContent,
  Typography,
  Box,
} from "@mui/material";

export default function StatisticsCard({
  title,
  value,
  icon,
}) {
  return (
    <Card
      elevation={4}
      sx={{
        borderRadius: 3,
        transition: "0.2s",
        "&:hover": {
          transform: "translateY(-3px)",
        },
      }}
    >
      <CardContent>

        <Box mb={2}>
          {icon}
        </Box>

        <Typography
          color="text.secondary"
        >
          {title}
        </Typography>

        <Typography
          variant="h4"
          fontWeight="bold"
        >
          {value}
        </Typography>

      </CardContent>
    </Card>
  );
}