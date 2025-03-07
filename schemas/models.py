from pydantic import BaseModel
from typing import List, Optional

class QueryAnalysis(BaseModel):
    main_topic: str
    subtopics: List[str] 
    information_type: str
    rephrased_query: Optional[str] = None

class RetrievedDocument(BaseModel):
    content: str
    source: str
    similarity: float

# ✅ Wrapper for List of Retrieved Documents
class RetrievedDocumentsResponse(BaseModel):
    documents: List[RetrievedDocument]

class AugmentedContext(BaseModel):
    original_query: str
    retrieved_information: RetrievedDocumentsResponse
    combined_context: str

# ✅ Wrapper for List of Strings (Sources)
class StringList(BaseModel):
    items: List[str]

class GeneratedResponse(BaseModel):
    response: str
    summary: str
    # sources: StringList 

class RAGResponse(BaseModel):
    final_answer: str
    # sources: Optional[StringList] = None
    # confidence: Optional[float] = None


