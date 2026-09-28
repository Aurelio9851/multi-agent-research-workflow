from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


def planner_agent(state):

    question = state["question"]

    prompt = f"""
    You are a scientific research planner.

    Given this research question:

    {question}

    Create a list of research aspects
    that should be investigated.
    """

    response = llm.invoke(prompt)


    return {
        "research_plan": [
            response.content
        ]
    }