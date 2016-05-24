# OpenSwitch Topology Modular Framework Common Code
A library for the Topology Modular Framework that contains code that can be shared between
repositories in OpenSwitch.

## Directory structure
```
.
|_ MAINTAINERS
|_ README.md
|_ doc
    |_ ... (other_doc_files)
|_ lib
  |_ topology_common
    |_ host
      |_ system
        |_ host_common_system_module.py
    |_ __init__.py (Python package init file)
    |_ ops
      |_ __init__.py (feature's specific Python package init file)
      |_ feature_a
        |_ feature_module.py
      |_ feature_b
      |_ system
        |_ ops_common_system_module.py
    |_ utils
      |_ common_utils_module.py
|_ ... (other_config_files)
|_ setup.py
|_ test
  |_ host
  |_ ops
    |_ feature_a
      |_ test_feature_a_module.py
  |_ utils
    |_ test_common_utils_module.py

```


Under the root directory several configuration files such as the `setup.py` script, the
`MANIFEST.in`, `requirements.txt` and others can be found.

The most important directories for developers contributing common code are `lib/topology_common/`
and `test/` where the production and test code live.


## Production code
The production code lives in  the `lib/topology_common` directory.

The common code can separated by the following criteria:

- Is the code specific to a linux host?
    - Create the files directly under `lib/topology_common/host`
- Is the code specific to OpenSwitch feature configuration and/or verification?
    - Create a file named after the feature and place it under
      `lib/topology_common/ops/<feature_path>`.
- Is the code generic, meaning can be used largely in all test cases (e.g. create MAC addresses,
  increment IP)?
    - Place the files directly under `lib/topology_common/util`


Example that contains code for the VLAN feature and common code for process, packet and file
management:

```
|_ lib
  |_ topology_common
    |_ host
      |_ file_management.py
    |_ ops
      |_ __init__.py (feature's specific Python package init file)
      |_ l2
        |_ vlan
          |_ vlan_db_access.py
          |_ vlan_management.py
        |_ system
          |_ process_management.py
    |_ utils
      |_ packet_management.py
```

** Note:**
For every new directory created under `lib/topology_common`, a new `__init__.py` (can be empty)
needs to be created under the directory, so that it is treated as a Python package.

## Using the library in feature or component tests
The Topology Common library is built and installed as a Python package for the tests if added to the
`requirements.txt` file.

1. Add the repo to the `tox` `requirements.txt` file, e.g.:
```
# Topology Common Code library
-e git+https://git.openswitch.net/openswitch/ops-topology-common@master#egg=topology_common
```

2. Import the modules of interest in the tests, e.g.:
```
from topology_common.ops.system import service as service
```
or
```
from topology_common.host import file_management
```

3. Use the code in the tests, e.g.:
```
    def test_verify_service_running():

        assert service.is_running("ops-my-service") is True
```

## Topology Common Code library tests
The library defines APIs that many tests will be using and depending on. As changes are added to the
library, the API may change and dependent tests may break. **As a responsible developer please
make sure to add tests along with the library contributions.**

The test code lives in  the `test/` directory.

The Topology Common library supports `pytest` and `tox`. The tests can be easily run from the repo's
root directory with the command:
```
tox
```

The `topology_common\lib` directory is a Python package and `tox` is responsible for installing the
package when running tests. Hence, in order to access the production code from the test code, simply
import the modules.

Example using the following structure:

```
|_ lib
  |_ topology_common
    |_ host
      |_ file_management.py
    |_ ops
      |_ __init__.py (feature's specific Python package init file)
      |_ l2
        |_ vlan
          |_ vlan_db_access.py
          |_ vlan_management.py
        |_ system
          |_ process_management.py
    |_ utils
      |_ packet_management.py
```

To access the production code from the `test_vlan.py` test file:

For code that's contained in a sub-directory:
```
from topology_common.ops.l2.vlan import vlan_db_access
```


## Contributing to the library
The following is expected with each contribution:

 1. Follow the coding guidelines defined in the [OPS Modular Framework
    Library Guidelines](ops-mf-library-guidelines.md) document.
 2. Self-documented code using docstrings.
 3. Tests for every new feature or change to existing features.
 4. All existing tests pass. Verify by running `tox` in the root of the repo before sending for
review.
