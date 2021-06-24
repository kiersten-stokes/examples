## Run notebook using papermill

### Overview

Use the [`Run notebook using papermill`](https://raw.githubusercontent.com/kubeflow/pipelines/1.4.1/components/notebooks/Run_notebook_using_papermill/component.yaml) to execute a notebook with parameters.

The example pipeline takes a notebook file, `hello.ipynb`, and a `Parameters` object that specifies a value for the `name` parameter. On execution, the value given in the `Parameters` object will be printed in the given notebook.

### Prerequisites

None. The example pipeline should work as is.

### Parameters
- Notebook
- Parameters
- Packages to install
- Input data
