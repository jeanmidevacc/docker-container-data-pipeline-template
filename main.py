import argparse

import functions as func


def get_arguments():# Function to get the argument provided with the python cmd
    parser = argparse.ArgumentParser(description='Collect new data')
    parser.add_argument('--config', type=str, help='Location of the configuration file of the pipeline', default="./config.json")
    parser.add_argument('--debug', help='Boolean to determine the mode of execution', action="store_true")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_arguments()
    print(args)
    new_data = func.get_new_data()# Just a random data collecter for the template
    print("DONE")