from llm.openrouter_client import generate_llm_followup

def generate_question(
    rule_type,
    evaluation,
    previous_question,
    candidate_answer
):

    # Stop interview
    if rule_type == "stop":
        return "Interview topic completed."

    try:

        llm_question = generate_llm_followup(
            previous_question,
            candidate_answer,
            evaluation
        )

        return llm_question

    except Exception as e:

        print("LLM Error:", e)

        # Fallback logic
        missing_topics = evaluation["missing_topics"]

        if rule_type == "clarification":
            return "Can you explain your answer in more detail?"

        elif rule_type == "off_topic":
            return "Can you focus more on the asked topic?"

        elif rule_type == "missing_topic":

            if len(missing_topics) > 0:
                return f"Can you explain more about {missing_topics[0]}?"

            return "Can you explain the missing concepts?"

        elif rule_type == "advanced":
            return "Can you provide a real-world example?"

        return "Can you elaborate further?"