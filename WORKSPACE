workspace(
    name = "meal_scheduler",
)

# These rules are built-into Bazel but we need to load them first to download more rules
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# NOTE: cannot use version 0.0.1 as it doesn't support Python 3 pip packages.
git_repository(
    name = "rules_python",
    commit = "708ed8679d7510a331ce9a7b910a2a056d24f7b1",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip3_import", "pip_repositories")

pip_repositories()

pip3_import(
    name = "my_deps",
    requirements = "//src:requirements.txt",
)

load("@my_deps//:requirements.bzl", "pip_install")

pip_install()
