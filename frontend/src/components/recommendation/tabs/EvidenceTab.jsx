import {
    List,
    ListItem,
    ListItemText,
    Typography
} from "@mui/material";

export default function EvidenceTab({ drug }) {

    const evidence = drug.evidence?.top_civic || [];

    if (evidence.length === 0)

        return (

            <Typography>

                No clinical evidence available.

            </Typography>

        );

    return (

        <List>

            {

                evidence.map((item, index) => (

                    <ListItem key={index}>

                        <ListItemText

                            primary={

                                item.disease ||

                                item.variant ||

                                "Clinical Evidence"

                            }

                            secondary={

                                item.evidence_type ||

                                item.evidence_level

                            }

                        />

                    </ListItem>

                ))

            }

        </List>

    );

}