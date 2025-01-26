import argparse
import cv2

parser = argparse.ArgumentParser("This is a Face Recognizer Program")
parser.add_argument("--encode", "-e", action='store_true')
parser.add_argument("--dataset", "-s", type=str, default="")
parser.add_argument("--encoded-data-file", "-r", type=str, default="")

parser.add_argument("--decode", "-d", action='store_true')
parser.add_argument("--encoded-file-name", "-o", type=str, default="")

args = parser.parse_args()

