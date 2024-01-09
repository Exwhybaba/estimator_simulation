import pandas as pd 
#import numpy as np
#import glob
import os
import random

path = r"C:\Users\Administrator\Documents\Dr Abidemi\Study CSP 1019\Data\CSV"

all_forms = glob.glob(path + '/*.csv')

def Simu(form_no, sample_no):
    """
    Generate simulated data with missing values based on the distribution of existing values.

    Parameters:
    - form_no (pd.DataFrame): The original DataFrame used as a template for generating simulated data.
    - sample_no (int): The number of samples to generate in the simulated data.

    Returns:
    pd.DataFrame: A DataFrame containing the simulated data with missing values.
    """

    # Extract column names from the original DataFrame
    form1Para = form_no.columns
    columns = form1Para

    # Create an empty DataFrame to store the simulated data
    formSimu = pd.DataFrame(columns=columns)

    # Calculate the percentage of missing values in each column
    missing_percentage = round(form_no.isnull().mean() * 100)

    # Create a placeholder array for the new generated values
    tmp = np.empty((sample_no, len(form1Para)), dtype="object")

    # Iterate through each column to generate simulated data
    for i in range(len(columns)):
        each_col = columns[i]
        unique_values = form_no[each_col].unique()

        # Calculate the target percentage of missing values for the current column
        target_missing_percentage = missing_percentage[each_col]
        nan_prob = target_missing_percentage / 100

        # Impute missing values based on the distribution of existing values
        existing_values = form_no[each_col].dropna()
        imputed_values = existing_values.sample(min(int((1 - nan_prob) * sample_no), len(existing_values)), replace=True).values

        # Calculate the probability distribution for sampling
        p_distribution = [1 - nan_prob] * len(imputed_values) + [nan_prob * len(unique_values)]

        # Randomly sample values from the imputed values and NaN values
        sampled_values = np.random.choice(
            np.concatenate([imputed_values, [np.nan]]),
            size=sample_no,
            replace=True,
            p=p_distribution / np.sum(p_distribution)  # Normalize probabilities to sum to 1
        )

        # Update the placeholder array with sampled values
        tmp[:, i] = sampled_values

    # Replace remaining None with a default value (change 'DefaultValue' to your desired default)
    tmp[tmp == None] = 'DefaultValue'

    # Populate the new DataFrame with the values from the placeholder array
    formSimu = pd.DataFrame(tmp, columns=columns)

    return formSimu



