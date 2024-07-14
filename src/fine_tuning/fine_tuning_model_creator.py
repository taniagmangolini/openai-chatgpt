"""See the docs: https://cookbook.openai.com/examples/chat_finetuning_data_prep"""

import os
import api
from logger import Logger


logger = Logger().get_logger()


FILE_PATH = os.path.join("fine_tuning/data/data.jsonl")


def upload_tuning_file(filepath):
    file_id = api.files_create(filepath, purpose="fine-tune")
    logger.info(f"Training file {file_id}")
    return file_id


def upload_tuning_job(file_id):
    fine_tune_job = api.fine_tuning_job_create(file_id)
    logger.info(f"Job {fine_tune_job}")
    return fine_tune_job


def check_tuning_status(fine_tune_job):
    """
    Once the fine-tuning process is complete, the CLI will display the name of your newly created model.
    OpenAI will also send you an email with the same information.
    You can now use your fine-tuned model!
    """
    logger.info("Validating files in progress...")
    while fine_tune_job.status == "validating_files":
        fine_tune_job = api.fine_tuning_job_retrieve(fine_tune_job.id)

    logger.info("Fine-tuning in progress...")
    while fine_tune_job.status == "running" or fine_tune_job.status == "queued":
        fine_tune_job = api.fine_tuning_job_retrieve(fine_tune_job.id)

    logger.info("Fine-tuning is complete!")
    logger.info(f"The name of the new model is: {fine_tune_job.fine_tuned_model}")


# upload the file
# file_id = upload_tuning_file(FILE_PATH)
# logger.info(f"Training file {file_id}")

# create a fine-tunning job
# fine_tune_job = upload_tuning_job(file_id)
# logger.info(f"Job {fine_tune_job}")

# check status for the fine-tunning job
# check_tuning_status(fine_tune_job)
