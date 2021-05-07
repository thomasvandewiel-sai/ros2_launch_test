import sys
import pickle
import numpy as np

MAX_ALLOWED_COMPUTATION_TIME = 0  # ms
MAX_ALLOWED_COMPUTATION_TIME_MEAN = 0  # ms
MAX_ALLOWED_COMPUTATION_TIME_STD = 0  # ms

MAX_ALLOWED_PREDICTION_ERROR = 0  # m
MAX_ALLOWED_PREDICTION_ERROR_MEAN = 0  # m
MAX_ALLOWED_PREDICTION_ERROR_STD = 0  # m


def main():

    # Load data
    with open("./dummy.pkl", "rb") as f:
        optimization_time, target_error = pickle.load(f)

    # Check whether we violate max/mean/std limits
    if (
        np.max(optimization_time) > MAX_ALLOWED_COMPUTATION_TIME
        or np.mean(optimization_time) > MAX_ALLOWED_COMPUTATION_TIME_MEAN
        or np.std(optimization_time) > MAX_ALLOWED_COMPUTATION_TIME_STD
        or np.max(target_error) > MAX_ALLOWED_PREDICTION_ERROR
        or np.mean(target_error) > MAX_ALLOWED_PREDICTION_ERROR_MEAN
        or np.std(target_error) > MAX_ALLOWED_PREDICTION_ERROR_STD
    ):
        return 1
    else:
        return 0


if __name__ == "__main__":

    status = main()

    print("Optimization-based action selection exiting with status: ", status)
    sys.exit(status)
