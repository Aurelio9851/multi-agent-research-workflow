from typing import TypedDict, List


class ResearchState(TypedDict):

    # domanda iniziale
    question: str

    # piano generato dal planner
    research_plan: List[str]

    # paper trovati
    papers: List[dict]

    # informazioni estratte dai paper
    context: List[str]

    # output finale
    report: str

    # qualtiy
    quality_score: int

    # review feedback
    review_feedback: str