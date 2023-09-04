#!/usr/bin/env python3

from kinematics_model_generator import parse_urdf, process_args

import sys


if __name__ == "__main__":
    opts, input_file_name = process_args(sys.argv[1:])
    parse_urdf(None, input_file_name, **vars(opts))
