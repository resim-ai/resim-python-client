# Copyright 2023 ReSim, Inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Macro to help bring in transitive dependencies of this workspace.
"""

load("@rules_python//python:pip.bzl", "pip_parse")

def resim_python_client_dependencies_2():
    """Macro to help bring in transitive dependencies of this workspace.
    """
    pip_parse(
        name = "resim_python_client_deps",
        requirements_lock = "@resim-python-client//:requirements.txt",
    )
