"""See the docs: https://cookbook.openai.com/examples/chat_finetuning_data_prep"""

import os
import api
from logger import Logger


logger = Logger().get_logger()


FILE_PATH = os.path.join("fine_tuning/data/data.jsonl")


# upload the file
file_id = api.files_create(FILE_PATH, purpose="fine-tune")
logger.info(f"Training file {file_id}")

# create a fine-tunning job
fine_tune_job = api.fine_tuning_job_create(file_id)
logger.info(f"Job {fine_tune_job}")

logger.info("Validating files in progress...")
while fine_tune_job.status == "validating_files":
    fine_tune_job = api.fine_tuning_job_retrieve(fine_tune_job.id)

logger.info("Fine-tuning in progress...")
while fine_tune_job.status == "running" or fine_tune_job.status == "queued":
    fine_tune_job = api.fine_tuning_job_retrieve(fine_tune_job.id)

"""
Once the fine-tuning process is complete, the CLI will display the name of your newly created model. 
OpenAI will also send you an email with the same information.
You can now use your fine-tuned model!
"""
logger.info("Fine-tuning is complete!")
logger.info(f"The name of the new model is: {fine_tune_job.fine_tuned_model}")
