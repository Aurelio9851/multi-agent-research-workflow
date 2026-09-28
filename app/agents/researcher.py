import arxiv


def researcher_agent(state):

    query = state["question"]


    search = arxiv.Search(
        query=query,
        max_results=5
    )


    papers = []

    for result in search.results():

        papers.append(
            {
                "title": result.title,
                "summary": result.summary,
                "url": result.entry_id
            }
        )


    return {
        "papers": papers
    }