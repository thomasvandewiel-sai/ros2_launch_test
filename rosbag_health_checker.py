import yaml
from yaml import CLoader as Loader
import os
import sys
import argparse


def main(bag, topics):

    stream = open(os.path.join(bag, "metadata.yaml"), "r")
    bag_metadata = yaml.load(stream, Loader=Loader)

    topics_passed = 0

    for topic in bag_metadata["rosbag2_bagfile_information"]["topics_with_message_count"]:
        if topic["topic_metadata"]["name"] in topics and topic["message_count"] > 0:
            topics_passed += 1
            print("Topic %s was published %d times" % (topic["topic_metadata"]["name"], topic["message_count"]))

    if topics_passed == len(topics):
        return 0
    return 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--bag_name", type=str, help="Full directory of the rosbag folder.")

    parser.add_argument(
        "--topic_checks", type=str, default="", nargs="+", help="List of topics to check the health status"
    )

    input_arguments = parser.parse_args()
    status = main(bag=input_arguments.bag_name, topics=input_arguments.topic_checks)

    print("Check script exiting with status: ", status)
    sys.exit(status)