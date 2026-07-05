import json
import time
from datetime import datetime

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

from app.core.config import settings
from app.schemas.api_response import APIResponse
from app.schemas.pipeline import PipelineRequest
from app.services.pipeline_service import PipelineService

router = APIRouter()

service = PipelineService()


@router.post(
    "/predict",
    response_model=APIResponse,
)
def predict(
    request: Request,
    body: PipelineRequest,
):
    start = time.perf_counter()

    context, report = service.analyze(body.genes)

    elapsed = (time.perf_counter() - start) * 1000

    sections = {
        "mutation_analysis": getattr(context, "mutation_analysis", None),
        "graph_analysis": getattr(context, "graph_analysis", None),
        "pathway_analysis": getattr(context, "pathway_analysis", None),
        "clinical_evidence": getattr(context, "evidence", None),
        "literature": getattr(context, "literature", None),
        "clinical_trials": getattr(context, "clinical_trials", None),
        "fusion": getattr(context, "fused_recommendations", None),
        "explanations": getattr(context, "explanations", None),
    }

    print("\n================ PIPELINE VALIDATION ================")

    for name, obj in sections.items():

        print(f"\nTesting {name}...")

        try:
            encoded = jsonable_encoder(obj)
            json.dumps(encoded, allow_nan=False)
            print(f"OK: {name}")

        except Exception as e:
            print(f"FAILED: {name}")
            print(e)

    recommendations = []

    for r in report.recommendations:

        recommendations.append(
            {
                "gene": r.gene,
                "drug": r.drug,
                "confidence": round(float(r.confidence), 4),

                "final_score": round(
                    float(getattr(r, "confidence", 0)),
                    4,
                ),

                "approved": getattr(
                    r,
                    "approved",
                    False,
                ),

                "immunotherapy": getattr(
                    r,
                    "immunotherapy",
                    False,
                ),

                "anti_neoplastic": getattr(
                    r,
                    "anti_neoplastic",
                    False,
                ),

                "drug_class": getattr(
                    r,
                    "drug_class",
                    None,
                ),

                "mechanism": getattr(
                    r,
                    "mechanism",
                    None,
                ),
            }
        )

    dashboard = {
        "genes": len(set(r["gene"] for r in recommendations)),
        "drugs": len(recommendations),
        "papers": len(getattr(context, "literature", []) or []),
        "trials": len(getattr(context, "clinical_trials", []) or []),
        "evidence": len(getattr(context, "evidence", []) or []),
    }

    metadata = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "pipeline_version": settings.API_VERSION,
        "processing_time_ms": round(elapsed, 2),
        "gene_count": len(body.genes),
        "recommendation_count": len(recommendations),
    }

    pipeline_profile = jsonable_encoder(
        getattr(context, "pipeline_profile", None)
    )

    response = {

        "metadata": metadata,

        "dashboard": dashboard,

        "pipeline_profile": pipeline_profile,

        "recommendations": recommendations,

        "mutation_analysis": jsonable_encoder(
            getattr(context, "mutation_analysis", None)
        ),

        "graph_analysis": jsonable_encoder(
            getattr(context, "graph_analysis", None)
        ),

        "pathway_analysis": jsonable_encoder(
            getattr(context, "pathway_analysis", None)
        ),

        "clinical_evidence": jsonable_encoder(
            getattr(context, "evidence", None)
        ),

        "literature": jsonable_encoder(
            getattr(context, "literature", None)
        ),

        "clinical_trials": jsonable_encoder(
            getattr(context, "clinical_trials", None)
        ),

        "fusion": jsonable_encoder(
            getattr(context, "fused_recommendations", None)
        ),

        "explanations": jsonable_encoder(
            getattr(context, "explanations", None)
        ),

        "report": jsonable_encoder(report),
    }
    print("\n========== RESPONSE KEYS ==========")
    print(response.keys())
    print("===================================\n")

    return APIResponse(
        success=True,
        request_id=request.state.request_id,
        api_version=settings.API_VERSION,
        processing_time_ms=round(elapsed, 2),
        data=response,
    )