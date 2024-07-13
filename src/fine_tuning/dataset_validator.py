import json
from collections import defaultdict
import os
from logger import Logger


logger = Logger().get_logger()


def validate_messages(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            dataset = [json.loads(line) for line in f]
        except:
            raise ValueError("The dataset must be a valid JSONL file")

        size = len(dataset)
        if size < 10:
            raise ValueError("The dataset must contain at least 10 examples")

        # validate the dataset content
        format_errors = defaultdict(int)

        for line in dataset:

            # Verify if each entry is a dictionary
            if not isinstance(line, dict):
                format_errors["data_type"] += 1
                continue

            # Check if there is a 'messages' list
            messages = line.get("messages", None)
            if not messages:
                format_errors["missing_messages_list"] += 1
                continue

            for message in messages:
                # Ensure each message has 'role' and 'content' keys
                if "role" not in message or "content" not in message:
                    format_errors["message_missing_key"] += 1

                # Valid keys that a message can contain
                valid_keys = ("role", "content", "name", "function_call")

                # Check for any keys not in valid_keys
                if any(k not in valid_keys for k in message):
                    format_errors["message_unrecognized_key"] += 1

                # Valid roles that a message can have
                valid_roles = ("system", "user", "assistant", "function")

                # Check if 'role' is one of the valid_roles
                if message.get("role", None) not in valid_roles:
                    format_errors["unrecognized_role"] += 1

                content = message.get("content", None)

                function_call = message.get("function_call", None)

            # Check if 'content' is textual and a string
            # Also, check if 'content' or 'function_call' is present
            if (not content and not function_call) or not isinstance(content, str):
                format_errors["missing_content"] += 1

        # Check if there is at least one assistant message
        if not any(message.get("role", None) == "assistant" for message in messages):
            format_errors["example_missing_assistant_message"] += 1

    # Print the errors, if any
    if format_errors:
        logger.info("Found errors:")
        for k, v in format_errors.items():
            print(f"{k}: {v}")
        raise ValueError("The dataset contains errors")
    else:
        logger.info("No errors were found.")
