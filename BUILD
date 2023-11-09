load("@rules_python//python:defs.bzl", "py_library")
load("@resim_python_client_deps//:requirements.bzl", "requirement")

py_library(
    name = "resim_python_client",
    srcs = glob(["resim_python_client/**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [
        requirement("openapi_python_client"),
    ],
)
