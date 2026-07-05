import { Box, Grid } from "@mui/material";

import ProfileSettings from "../components/settings/ProfileSettings";
import AISettings from "../components/settings/AISettings";
import DatabaseSettings from "../components/settings/DatabaseSettings";
import PipelineSettings from "../components/settings/PipelineSettings";
import NotificationSettings from "../components/settings/NotificationSettings";
import SecuritySettings from "../components/settings/SecuritySettings";
import AppearanceSettings from "../components/settings/AppearanceSettings";
import SystemInformation from "../components/settings/SystemInformation";
import SaveSettingsButton from "../components/settings/SaveSettingsButton";

export default function Settings() {
  return (
    <Box>

      <Grid container spacing={3}>

        <Grid size={{ xs:12, md:6 }}>
          <ProfileSettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <AppearanceSettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <AISettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <PipelineSettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <DatabaseSettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <NotificationSettings />
        </Grid>

        <Grid size={{ xs:12, md:6 }}>
          <SecuritySettings />
        </Grid>

        <Grid size={{ xs:12 }}>
          <SystemInformation />
        </Grid>

        <Grid size={{ xs:12 }}>
          <SaveSettingsButton />
        </Grid>

      </Grid>

    </Box>
  );
}