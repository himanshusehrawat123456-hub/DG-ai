"""
DG AI Version 1
Search Filter

Purpose:
- Filter search results
- Apply keyword filtering

Version: 1.0
"""


class SearchFilter:
    """
    Handles search result filtering.
    """

    def filter_results(self, results, keyword):
        """
        Return filtered results.
        """

        filtered = []

        for item in results:

            if keyword.lower() in item.lower():

                filtered.append(item)

        return filtered


# Testing

if __name__ == "__main__":

    search_filter = SearchFilter()

    data = [
        "Python Tutorial",
        "Java Programming",
        "Python Functions",
        "AI Development"
    ]

    print(
        search_filter.filter_results(
            data,
            "Python"
        )
    )
