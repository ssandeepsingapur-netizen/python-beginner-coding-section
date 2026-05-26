import wikipedia as wiki
def get_Wikipedia_summary(topic):
    try:
        summary = wiki.summary(topic)
        return summary
    except wiki.exceptions.DisambiguationError as e:
        return f"Topic '{topic}' is ambiguous. Possible options: {e.options}"
    except wiki.exceptions.PageError:
        return f"Topic '{topic}' not found on Wikipedia."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

    # example usage
topic = "virat kohli"
summary = get_wikipedia_summary(topic)
print(summary)