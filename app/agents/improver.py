from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-mini"
)



def improvement_agent(state):

    report = state["report"]

    feedback = state["review_feedback"]


    prompt = f"""

Improve this scientific review.

Current report:

{report}


Reviewer feedback:

{feedback}

Generate a better version.

"""


    response = llm.invoke(prompt)


    return {

        "report": response.content

    }