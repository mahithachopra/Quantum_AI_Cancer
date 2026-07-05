import { useState } from "react";

import {
    Tabs,
    Tab,
    Box
} from "@mui/material";

import OverviewTab from "./tabs/OverviewTab";
import EvidenceTab from "./tabs/EvidenceTab";
import LiteratureTab from "./tabs/LiteratureTab";
import TrialTab from "./tabs/TrialTab";
import MechanismTab from "./tabs/MechanismTab";

export default function DrugTabs({ drug }) {

    const [tab, setTab] = useState(0);

    return (

        <Box mt={2}>

            <Tabs
                value={tab}
                onChange={(e, value) => setTab(value)}
                variant="scrollable"
                scrollButtons="auto"
            >

                <Tab label="Overview" />
                <Tab label="Evidence" />
                <Tab label="Literature" />
                <Tab label="Trials" />
                <Tab label="Mechanism" />

            </Tabs>

            <Box mt={3}>

                {tab === 0 && <OverviewTab drug={drug} />}
                {tab === 1 && <EvidenceTab drug={drug} />}
                {tab === 2 && <LiteratureTab drug={drug} />}
                {tab === 3 && <TrialTab drug={drug} />}
                {tab === 4 && <MechanismTab drug={drug} />}

            </Box>

        </Box>

    );

}