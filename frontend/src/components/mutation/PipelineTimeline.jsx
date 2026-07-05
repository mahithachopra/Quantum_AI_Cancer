import {
  Card,
  CardContent,
  Typography,
  Stepper,
  Step,
  StepLabel,
} from "@mui/material";

const steps=[

  "Mutation Detection",

  "Knowledge Base",

  "Drug Ranking",

  "Evidence Mining",

  "Literature Search",

  "Clinical Trials",

];

export default function PipelineTimeline(){

  return(

    <Card>

      <CardContent>

        <Typography
          variant="h6"
          gutterBottom
        >

          AI Pipeline

        </Typography>

        <Stepper
          activeStep={steps.length}
          orientation="vertical"
        >

          {steps.map(step=>(

            <Step
              key={step}
              completed
            >

              <StepLabel>

                {step}

              </StepLabel>

            </Step>

          ))}

        </Stepper>

      </CardContent>

    </Card>

  );

}