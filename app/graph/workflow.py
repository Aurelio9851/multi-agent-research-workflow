from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState

from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.writer import writer_agent
from app.agents.reviewer import reviewer_agent
from app.agents.improver import improvement_agent

from app.graph.router import review_router


workflow = StateGraph(ResearchState)



workflow.add_node(
    "planner",
    planner_agent
)


workflow.add_node(
    "researcher",
    researcher_agent
)


workflow.add_node(
    "writer",
    writer_agent
)



workflow.set_entry_point(
    "planner"
)



workflow.add_edge(
    "planner",
    "researcher"
)


workflow.add_edge(
    "researcher",
    "writer"
)


workflow.add_edge(
    "writer",
    "reviewer"
)

workflow.add_conditional_edges(

    "reviewer",

    review_router,

    {

        "approved": END,

        "improve": "improver"

    }

)

workflow.add_edge(
    "improver",
    "reviewer"
)


graph = workflow.compile()

