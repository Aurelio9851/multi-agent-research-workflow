from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


def writer_agent(state):

    papers = state["papers"]


    prompt = f"""

    Write a scientific literature review.

    Papers:

    {papers}

    Include:
    - main approaches
    - comparison
    - limitations
    - future directions

    """


    response = llm.invoke(prompt)


    return {
        "report": response.content
    }