import argparse


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i",
                           "--image",
                           default=None,
                           help="path to Image File ")
    arg_parse.add_argument("-o",
                           "--output",
                           type=str,
                           help="path to optional output video file")
    args = vars(arg_parse.parse_args())
    return args
