import numpy as np

def generate_data(n=1000, mean=0, std=1):
    return np.random.normal(loc=mean, scale=std, size=n)

def analyze_data(data):
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
    }

