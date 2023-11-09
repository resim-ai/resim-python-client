# Copyright 2023 ReSim, Inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Macro to help bring in transitive dependencies of this workspace.
"""

load("@resim_python_client_deps//:requirements.bzl", "install_deps")

def resim_python_client_dependencies_3():
    """Macro to help bring in transitive dependencies of this workspace.
    """
    install_deps()
