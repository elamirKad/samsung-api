import pickle
import openai


def load_chat_log(story_id):
    """
    Load the chat log for the given story ID.
    """
    chat_log_path = f"chat_logs/{story_id}.pkl"
    try:
        with open(chat_log_path, "rb") as f:
            return pickle.load(f)
    except:
        return []


def save_chat_log(story_id, chat_log):
    """
    Save the chat log for the given story ID.
    """
    chat_log_path = f"chat_logs/{story_id}.pkl"
    with open(chat_log_path, "wb") as f:
        pickle.dump(chat_log, f)


def get_full_story(chat_log):
    """
    Returns the full story as a string from the chat log.
    """
    full_story = ""
    for assistant_message in chat_log[1::2]:
        message_list = assistant_message["content"].split("\n")[4:]
        if message_list[-1].startswith("3)"):
            message_list = message_list[:-4]
        full_story += "\n".join(message_list)
    return full_story


def get_choices(continuation):
    """
    Returns a list of the choices in the given continuation.
    """
    return [line[3:][:-1] for line in continuation.split("\n") if line.startswith(("1)", "2)", "3)"))]


def generate_story(choice, story_id):
    """
    Generates a story continuation based on the given choice and user ID.
    """
    openai.api_key = "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"
    chat_log = load_chat_log(story_id)
    chat_log.append({"role": "user", "content": choice})

    messages = [
        {"role": "system", "content": "You are an elderly storyteller, captivating a young child with an enchanting tale. The very first prompt will have the format:\n\"Tell a story about ... (Child's name is ...)\".\n- The child assumes the role of the main protagonist.\n- You should briefly describe the protagonists visual look.\n- You will craft a brief continuation of the plot, prompting the user to describe the protagonist's actions. You should provide exactly THREE story continuations in the following format:\n'''\nWhat should ... do?\n1) Action one;\n2) Action two;\n3) Action three.\n'''\nFollow this rule carefully!\n- Do not wrap the choices in quotation marks.\n- The continuation should be 5-8 sentences long.\n- After receiving their input, incorporate the chosen action into the story and continue in this manner.\n- Following exactly FOUR (no more, no less) story continuations, the adventure should reach its thrilling conclusion.\n- The story should be appropriate for a child under the age of 10.\n- The story should be written in the third person and active voice."},
    ]
    messages = messages + chat_log

    continuation = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=512,
        messages=messages,
    )["choices"][0]["message"]["content"]

    chat_log.append({"role": "assistant", "content": continuation})
    save_chat_log(story_id, chat_log)

    return continuation, get_choices(continuation)
