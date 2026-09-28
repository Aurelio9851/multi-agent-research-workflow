def review_router(state):

    score = state["quality_score"]


    if score >= 80:

        return "approved"

    else:

        return "improve"