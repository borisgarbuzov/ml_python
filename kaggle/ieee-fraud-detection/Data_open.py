import pandas as pd

test_identity = pd.read_csv("test_identity_truncated.csv")
print(test_identity, "\n")
print(test_identity.columns)

sample_submission = pd.read_csv("sample_submission_truncated.csv")
print(sample_submission, "\n")
print(sample_submission.columns)

test_transaction_truncated = pd.read_csv("test_transaction_truncated.csv")
print(test_transaction_truncated, "\n")
print(test_transaction_truncated.columns)

train_transaction_truncated = pd.read_csv("train_transaction_truncated.csv")
print(train_transaction_truncated, "\n")
print(train_transaction_truncated.columns)


