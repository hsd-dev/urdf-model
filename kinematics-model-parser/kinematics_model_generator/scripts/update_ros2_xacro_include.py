#!/usr/bin/env python3

from itertools import count, takewhile
import sys


if __name__ == "__main__":
    filepath = sys.argv[1]
    package = sys.argv[2]
    ros2_control_path = sys.argv[3].rstrip('/')

    with open(filepath) as f:
        control_xacro = f.readlines()

        for i, line in zip(count(), control_xacro):
            if 'ros2_control.xacro' in line:
                whitespace = list(takewhile(str.isspace, line))
                control_xacro[i] = ''.join(whitespace) + f'<xacro:include filename="$(find {package})/{ros2_control_path}" />'

            if 'xacro:' in line and '_ros2_control name=' in line:
                del(control_xacro[i])

    with open(filepath, 'w') as f:
        f.writelines(control_xacro)
