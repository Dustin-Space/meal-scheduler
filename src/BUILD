# load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_library", "py_proto_compile")
load("@rules_python//python:python.bzl", "py_binary", "py_library")
load("@my_deps//:requirements.bzl", "requirement")

# py_proto_compile(
#   name = "inventory_py_pb_compile",
#   protos = ["inventory.proto"],
#   with_grpc = False,
# )

#py_proto_library(
#  name = "inventory_py_pb",
#  protos = ["inventory.proto"],
#  with_grpc = False,
#)

# Define a py_binary rule and include the grpcio package as a dependency.
py_binary(
    name = "meal_scheduler",
    srcs = [
        "meal_scheduler.py",
    ],
    deps = [
        #":inventory_py_pb2",
        #requirement("protobuf"),
	requirement("absl-py"),
    ],
)
