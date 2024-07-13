# Model training

Before fine-tuning a model, it’s necessary to consider the costs associated with training, input usage, and output.

When you train (or fine-tune) a model, you’re essentially updating its parameters to better suit your data and use case. The cost is calculated based on the number of tokens in your training dataset and is charged per 1,000 tokens (Training Cost is a one-time expense).

OpenAI suggests fine-tuning without specifying any hyperparameters, allowing the model to choose default values based on the size of the dataset. 

If the results still don’t meet your expectations, you can then adjust the number of epochs, learning rate multiplier, and batch size.

The process of adjusting the number of epochs (and any hyperparameter tuning in general) is iterative. You should start with a small number of epochs and gradually increase it until you achieve the desired results. If you notice that the model is overfitting and/or lacking diversity, you should reduce the number of epochs slightly, test, and repeat as necessary.

To pass hyperparameters to the model:

```
client.fine_tuning.jobs.create(
  training_file=file_id,
  model=model, 
  validation_file=validation_file_id,
  hyperparameters={
    "n_epochs": 10,
     "learning_rate_multiplier": 1.5,
     "batch_size": 32,

  }
)
```

# Token Limit

The maximum number of tokens per message depends on the model you choose. 

For GPT-3.5-Turbo, the maximum number of tokens per message is 16,385. 

For GPT-3.5-Turbo-0613, the maximum number of tokens per message is 4,096. 

If a message exceeds the maximum number of tokens, it will be truncated to fit within the limit, which may result in a loss of information.

# Dataset 

### Size

A minimum of 10 examples is required, but OpenAI recommends using at least 50 to 100 examples with GPT-3.5-Turbo.

The maximum file upload size is 1 GB.


### Quality

It’s important to ensure the data is clean, relevant, and well-structured.

If you’re creating a chatbot for a specific domain, you should start by clearly defining the following elements:

- The domain: Identify the specific field or area your chatbot will specialize in.

- Specify the issues or queries your chatbot is designed to handle.

- Define who your chatbot is intended for.

- Specify the language(s) that will support.

- The tone: Decide on the tone your chatbot’s responses should have (professional, informative, casual, playful, etc).

### Use a Validation Set

It is used to evaluate the model’s performance during the training process. 
Its main roles include tuning the model’s hyperparameters and helping to prevent overfitting by providing feedback on how the model performs on data it hasn’t seen during training.
To use a validation set, first upload it to the OpenAI api. Get the id for the file uploaded and use it as input for the fine tunning job.

'''
files.create(
  file=open(
    validation_file_path,
    "rb"
  ),
  purpose="fine-tune"
)
'''

### Test the Model
It’s advisable to split the initial dataset into two parts: training and testing.

One metric for assessing the training is the loss value. The training loss is a numerical measure of how well the model fits the training data.
A lower loss value generally indicates better model performance.

Below is an exemple of how to get this metric:

```
  events = client.fine_tuning.jobs.list_events(job_id)
  for event in events.data:
      if event.type == 'metrics':
          step = event.data['step']
          train_loss = event.data['train_loss']
          print(f"Step {step}: training loss={train_loss}")
```