#
# Copyright 2018-2022 Elyra Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from setuptools import find_packages, setup

long_desc = """
            Elyra component catalog connector for Artifactory
            """

here = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(here, "artifactory_catalog_connector", "_version.py")) as f:
    exec(f.read(), {}, version_ns)

setup_args = dict(
    name="elyra-artifactory-catalog-connector",
    version=version_ns["__version__"],
    url="https://github.com/elyra-ai/examples/tree/main/component-catalog-connectors/artifactory-connector",
    description="Elyra component catalog connector for Artifactory",
    long_description=long_desc,
    author="Elyra Maintainers",
    license="Apache License Version 2.0",
    packages=find_packages(),
    install_requires=[],
    setup_requires=["flake8"],
    include_package_data=True,
    entry_points={
        "metadata.schemas_providers": [
            "artifactory-catalog-schema = "
            "artifactory_catalog_connector.artifactory_schema_provider:ArtifactorySchemasProvider"
        ],
        "elyra.component.catalog_types": [
            "artifactory-catalog = "
            "artifactory_catalog_connector.artifactory_catalog_connector:ArtifactoryComponentCatalogConnector"
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

if __name__ == "__main__":
    setup(**setup_args)
