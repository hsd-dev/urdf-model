#!/usr/bin/env python3

from itertools import count, takewhile
import sys


if __name__ == "__main__":
    # this is the xacro from the generated MCP
    # since the package is generated, the path can be hardcoded
    xacropath = sys.argv[1]

    # this is the one to be included in the above file
    # it would include the package name as well
    # e.g. prbt_robot_support/urdf/prbt.ros2_control.xacro
    # this path has be to be converted in the form
    # "$(find prbt_robot_support)/urdf/prbt.ros2_control.xacro
    ros2control_path = sys.argv[2].rstrip('/')
    package = ros2control_path.split('/')[0]
    ros2control_path = ros2control_path.split('/', 1)[1]

    with open(xacropath) as f:
        control_xacro = f.readlines()

        for i, line in zip(count(), control_xacro):
            if 'ros2_control.xacro' in line:
                whitespace = list(takewhile(str.isspace, line))
                control_xacro[i] = ''.join(whitespace) + f'<xacro:include filename="$(find {package})/{ros2control_path}" />'

            if 'xacro:' in line and '_ros2_control name=' in line:
                del(control_xacro[i])

    with open(xacropath, 'w') as f:
        f.writelines(control_xacro)
