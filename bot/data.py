import os
import pandas as pd

class Dataset:
    """Wrapper for the DataFrame to return values similar 
    to `AbstractJokeGenerator` output.
    """

    def __init__(self, dataset_path, default_promt_token, answer_token):
        self.default_promt_token = default_promt_token
        self.answer_token = answer_token
        self.name = os.path.split(dataset_path)[1]
        self.data = pd.read_csv(dataset_path)

    def __getitem__(self, idx):
        question = self.data['Question'].iloc[idx].strip()
        answer = self.data['Answer'].iloc[idx].strip()
        text = (self.default_promt_token + question + '\n'
                + self.answer_token + ' ' + answer)
        return {
            'text': text,
            'generated_by': self.name,
        }

    def __len__(self):
        return len(self.data)

class Joke:
    """An interface class for a Joke."""
    def __init__(self, text, id):
        self.id = id
        self.text = text
