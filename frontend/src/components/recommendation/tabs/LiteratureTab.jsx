import {
    Card,
    CardContent,
    Typography
} from "@mui/material";

export default function LiteratureTab({ drug }) {

    const papers = drug.evidence?.top_papers || [];

    if (!papers.length)

        return (

            <Typography>

                No literature found.

            </Typography>

        );

    return (

        <>

            {

                papers.map(

                    (paper, index) => (

                        <Card
                            key={index}
                            sx={{ mb: 2 }}
                        >

                            <CardContent>

                                <Typography
                                    fontWeight="bold"
                                >

                                    {paper.title}

                                </Typography>

                                <Typography>

                                    {paper.journal}

                                </Typography>

                                <Typography>

                                    {paper.year}

                                </Typography>

                            </CardContent>

                        </Card>

                    )

                )

            }

        </>

    );

}