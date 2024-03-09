from src import example_package_samuelhomberg
with open("version.semver", "w") as f:
    f.write(example_package_samuelhomberg.__version__)