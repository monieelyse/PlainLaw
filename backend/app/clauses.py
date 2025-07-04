from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import re

router = APIRouter(
    prefix="/clauses",
    tags=["clauses"],
)

class OCRRequest(BaseModel):
    text: str

class Clause(BaseModel):
    clause_id: str
    content: str

@router.post("/", response_model=List[Clause])
def extract_clauses(request: OCRRequest):
    """
    Extracts individual clauses from the given text.
    A clause is defined as any block starting with the word 'Clause' followed by a number.
    """
    # 1) Regex to grab each “Clause X …” block, non-greedy up to the next “Clause” or the end
    pattern = r"(?ms)(Clause\s*\d+[\s\S]*?)(?=Clause\s*\d+|$)"
    matches = re.findall(pattern, request.text)

    if not matches:
        # If nothing matched, return a 400 with an error message
        raise HTTPException(status_code=400, detail="No clauses found in text")

    # 2) Build up a list of Clause models
    clauses: List[Clause] = []
    for clause_text in matches:
        # Use the first line (“Clause 1.”) as the ID
        first_line = clause_text.strip().splitlines()[0]
        clauses.append(
            Clause(
                clause_id=first_line,
                content=clause_text.strip()
            )
        )

    return clauses
