from setuptools import setup, find_packages

setup(
    author="Charles Titus",
    author_email="charles.titus@nist.gov",
    install_requires=["bluesky", "ophyd", "sst_base"],
    name="sst_common",
    use_scm_version=True,
    packages=find_packages()
)
