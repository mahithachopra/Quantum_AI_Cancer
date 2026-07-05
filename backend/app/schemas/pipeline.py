from pydantic import BaseModel
from typing import List


class PipelineRequest(BaseModel):

    genes: List[str]