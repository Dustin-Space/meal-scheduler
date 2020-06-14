# load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_library", "py_proto_compile")
load("@rules_python//python:python.bzl", "py_binary", "py_library")
load("@my_deps//:requirements.bzl", "requirement")

load("@build_stack_rules_proto//python:python_proto_library.bzl", "python_proto_library")
load("@protobuf_py_deps//:requirements.bzl", protobuf_requirement = "requirement")

proto_library(
    name = "inventory_proto",
    srcs = ["inventory.proto"],
)
# "@com_google_protobuf//:any_proto",

python_proto_library(
name = "inventory_py_proto",
    deps = [":inventory_proto"],
)


# Define a py_binary rule and include the grpcio package as a dependency.
py_binary(
    name = "meal_scheduler",
    srcs = [
        "meal_scheduler.py",
    ],
    deps = [
        ":inventory_py_proto",
        ":person_python_library",
        requirement("protobuf"),
        #protobuf_requirement("protobuf"),
	requirement("absl-py"),
    ],
)

python_proto_library(
    name = "person_python_library",
    deps = ["@build_stack_rules_proto//example/proto:person_proto"],
)
