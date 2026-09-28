from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


def reviewer_agent(state):

    report = state["report"]


    prompt = f"""

You are a scientific reviewer.

Evaluate this literature review:

{report}


Give:

1. Quality score from 0 to 100
2. Short feedback


Format:

SCORE: number

FEEDBACK:
text

"""


    response = llm.invoke(prompt)


    text = response.content


    # esempio parsing semplice
    score = 50

    if "90" in text:
        score = 90
    elif "80" in text:
        score = 80


    return {

        "quality_score": score,

        "review_feedback": text

    }