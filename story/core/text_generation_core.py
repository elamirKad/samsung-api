import pickle
import openai


def get_chat_log_path(story_id):
    """
    Returns the path to the chat-log pickle file for the given user.
    """
    return f"chat_logs/{story_id}.pkl"


def parse_continuation(continuation):
    """
    Returns a list of the choices in the given continuation.
    """
    continuation_list = continuation.split("\n")
    choices = []

    for line in continuation_list:
        if line.startswith("1)") or line.startswith("2)") or line.startswith("3)"):
            line = line[3:][:-1]  # remove the number and semicolon
            choices.append(line)

    return choices


def generate_story(choice, story_id):
    """
    Generates a story continuation based on the given choice and user ID.
    """
    chat_log_path = get_chat_log_path(story_id)
    try:  # load previous chat-log from pickle file if it exists
        with open(chat_log_path, "rb") as f:
            chat_log = pickle.load(f)
    except:  # otherwise, create a new chat-log
        chat_log = []

    chat_log.append({"role": "user", "content": choice})

    messages = [
        {"role": "system",
         "content": "You are an elderly storyteller, captivating a young child with an enchanting fantasy tale. The very first prompt will have the format:\n\"Tell a story about ... (Child's name is ...)\".\n- The child assumes the role of the main protagonist.\n- You will craft a brief continuation of the plot, prompting the user to describe the protagonist's actions. You should provide exactly THREE story continuations in the following format:\nWhat should ... do?\n1) Action one;\n2) Action two;\n3) Action three.\nFollow this rule carefully!\n- The continuation should be 5-10 sentences long.\n- After receiving their input, incorporate the chosen action into the story and continue in this manner.\n- Following exactly FIVE (no more, no less) story continuations, the adventure should reach its thrilling conclusion.\n- The story should be appropriate for a child under the age of 10.\n- The story should be written in the third person and active voice."},
    ]
    messages = messages + chat_log

    continuation = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=256,
        messages=messages,
    )["choices"][0]["message"]["content"]

    # append the continuation to the chat-log
    chat_log.append({"role": "assistant", "content": continuation})

    # save the chat-log to a pickle file
    with open(chat_log_path, "wb") as f:
        pickle.dump(chat_log, f)

    return continuation
