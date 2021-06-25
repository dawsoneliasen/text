workspace(name = "org_tensorflow_text")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

# git_repository(
#     name = "rules_cc",
#     commit = "daf6ace7cfeacd6a83e9ff2ed659f416537b6c74",
#     remote = "https://github.com/bazelbuild/rules_cc.git"
# )
# load("@rules_cc//cc:repositories.bzl", "rules_cc_dependencies", "rules_cc_toolchains")
# rules_cc_dependencies()
# rules_cc_toolchains()

# git_repository(
#     name = "bazel_skylib",
#     remote = "https://github.com/bazelbuild/bazel-skylib.git",
#     commit = "c6f6b5425b232baf5caecc3aae31d49d63ddec03"
# )
# load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
# bazel_skylib_workspace()

git_repository(
    name = "rules_proto",
    commit = "cfdc2fa31879c0aebe31ce7702b1a9c8a4be02d2",
    remote = "https://github.com/bazelbuild/rules_proto.git",
)

load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
rules_proto_dependencies()
rules_proto_toolchains()
 
load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
protobuf_deps()

http_archive(
    name = "com_google_sentencepiece",
    strip_prefix = "sentencepiece-1.0.0",
    sha256 = "c05901f30a1d0ed64cbcf40eba08e48894e1b0e985777217b7c9036cac631346",
    urls = [
        "https://github.com/google/sentencepiece/archive/1.0.0.zip"
    ],
    patches = ["//third_party/sentencepiece:processor.patch"],
    patch_args = ["-p1"],
)

http_archive(
    name = "icu",
    strip_prefix = "icu-release-64-2",
    sha256 = "dfc62618aa4bd3ca14a3df548cd65fe393155edd213e49c39f3a30ccd618fc27",
    urls = [
        "https://storage.googleapis.com/mirror.tensorflow.org/github.com/unicode-org/icu/archive/release-64-2.zip",
        "https://github.com/unicode-org/icu/archive/release-64-2.zip",
    ],
    build_file = "//third_party/icu:BUILD.bzl",
    patches = ["//third_party/icu:udata.patch"],
    patch_args = ["-p1"],
)

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "5b00383d08dd71f28503736db0500b6fb4dda47489ff5fc6bed42557c07c6ba9",
    strip_prefix = "rules_closure-308b05b2419edb5c8ee0471b67a40403df940149",
    urls = [
        "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",  # 2019-06-13
    ],
)

# NOTE: according to
# https://docs.bazel.build/versions/master/external.html#transitive-dependencies
# we should list the transitive dependencies of @org_tensorflow_hub in this
# WORKSPACE file.  Still, all of them are already listed by tf_workspace() which
# is called later in this file.
http_archive(
    name = "org_tensorflow_hub",
    strip_prefix = "hub-0.8.0",
    sha256 = "968af30c448d51c36501b68df2c916fb4a61007db3240adc9248fa3a9be2da6f",
    urls = [
        "https://github.com/tensorflow/hub/archive/v0.8.0.zip"
    ],
)

# http_archive(
#     name = "org_tensorflow",
#     strip_prefix = "tensorflow-2.5.0",
#     sha256 = "e3d0ee227cc19bd0fa34a4539c8a540b40f937e561b4580d4bbb7f0e31c6a713",
#     urls = [
#         "https://github.com/tensorflow/tensorflow/archive/v2.5.0.zip"
#     ],
#     patches = ["//third_party/tensorflow:tf.patch"],
#     patch_args = ["-p1"],
# )
git_repository(
    name = "org_tensorflow",
    remote = "https://github.com/kulinseth/tensorflow.git",
    branch = "master"
    # patches = ["//third_party/tensorflow:tf.patch"],
    # patch_args = ["-p1"],
)

http_archive(
    name = "org_tensorflow_datasets",
    sha256 = "c6ff4e2306387f0ca45d4f616d9a1c5e79e02ef16d0a8958230a8049ea07fc98",
    strip_prefix = "datasets-3.2.0",
    urls = [
        "https://github.com/tensorflow/datasets/archive/v3.2.0.zip",
    ],
)

# load(
#     "@rules_cc//cc:defs.bzl",
#     _cc_binary = "cc_binary",
#     _cc_import = "cc_import",
#     _cc_library = "cc_library",
#     _cc_test = "cc_test",
# )
# load(
#     "@rules_cc//examples:experimental_cc_shared_library.bzl",
#     _cc_shared_library = "cc_shared_library",
# )


load("@org_tensorflow//tensorflow:workspace3.bzl", "workspace")
workspace()
load("@org_tensorflow//tensorflow:workspace2.bzl", "workspace")
workspace()
load("@org_tensorflow//tensorflow:workspace1.bzl", "workspace")
workspace()
load("@org_tensorflow//tensorflow:workspace0.bzl", "workspace")
workspace()

load("//third_party/tensorflow:tf_configure.bzl", "tf_configure")

tf_configure(name = "local_config_tf")

# Set up Android.
load("@org_tensorflow//third_party/android:android_configure.bzl", "android_configure")
android_configure(name="local_config_android")
load("@local_config_android//:android.bzl", "android_workspace")
android_workspace()
