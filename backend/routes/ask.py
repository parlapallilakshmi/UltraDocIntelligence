from fastapi import APIRouter
from backend.services.retrieval import retrieve_docs
from backend.services.llm import generate_answer
from backend.services.guardrails import apply_guardrails
from backend.services.highlighter import highlight_text
from backend.services.confidence import calculate_confidence

router = APIRouter()


from backend.models.schemas import AskRequest, AskResponse

@router.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):

    docs, scores = retrieve_docs(req.question)


    context = "\n".join([d.page_content for d in docs])

    answer = generate_answer(context, req.question)

    answer, valid = apply_guardrails(answer, scores)

    highlighted_sources = [
        highlight_text(d.page_content, answer)
        for d in docs
    ]

    confidence = calculate_confidence(scores, highlighted_sources)

    return AskResponse(
        answer=answer,
        sources=highlighted_sources,
        confidence=confidence
    )