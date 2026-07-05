import {
  Card,
  CardContent,
  Button,
  Stack,
} from "@mui/material";

import html2canvas from "html2canvas";
import jsPDF from "jspdf";

export default function ExportButtons({
  pipeline,
  reportRef,
}) {
  const downloadPDF = async () => {
    if (!reportRef?.current) {
      alert("Report not found");
      return;
    }

    const canvas = await html2canvas(reportRef.current, {
      scale: 2,
      useCORS: true,
      scrollY: -window.scrollY,
    });

    const imgData = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p", "mm", "a4");

    const pageWidth = 210;
    const pageHeight = 297;

    const imgWidth = pageWidth;
    const imgHeight =
      (canvas.height * imgWidth) / canvas.width;

    let heightLeft = imgHeight;
    let position = 0;

    pdf.addImage(
      imgData,
      "PNG",
      0,
      position,
      imgWidth,
      imgHeight
    );

    heightLeft -= pageHeight;

    while (heightLeft > 0) {
      position = heightLeft - imgHeight;

      pdf.addPage();

      pdf.addImage(
        imgData,
        "PNG",
        0,
        position,
        imgWidth,
        imgHeight
      );

      heightLeft -= pageHeight;
    }

    const gene =
      pipeline.recommendations?.[0]?.gene || "Patient";

    pdf.save(
      `Clinical_Report_${gene}.pdf`
    );
  };

  const printReport = () => {
    window.print();
  };

  const exportCSV = () => {
    if (!pipeline?.recommendations?.length) {
      alert("No recommendations available.");
      return;
    }

    const rows = pipeline.recommendations.map((item) => ({
      Gene: item.gene,
      Drug: item.drug,
      Confidence: item.confidence,
      FDA: item.approved ? "Yes" : "No",
      DrugClass: item.drug_class || "",
      Mechanism: item.mechanism || "",
    }));

    const headers = Object.keys(rows[0]);

    const csv = [
      headers.join(","),
      ...rows.map((row) =>
        headers
          .map((field) => `"${row[field]}"`)
          .join(",")
      ),
    ].join("\n");

    const blob = new Blob([csv], {
      type: "text/csv;charset=utf-8;",
    });

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "Drug_Recommendations.csv";

    link.click();

    URL.revokeObjectURL(url);
  };

  return (
    <Card>
      <CardContent>
        <Stack direction="row" spacing={2}>
          <Button
            variant="contained"
            onClick={downloadPDF}
          >
            Download PDF
          </Button>

          <Button
            variant="outlined"
            onClick={printReport}
          >
            Print
          </Button>

          <Button
            variant="outlined"
            onClick={exportCSV}
          >
            Export CSV
          </Button>
        </Stack>
      </CardContent>
    </Card>
  );
}