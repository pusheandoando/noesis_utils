# Noesis Utils
Utility library for the Noesis Project.





## Installation
```bash
pip3 install --upgrade git+https://github.com/pusheandoando/noesis_utils.git
```





## Usage
### `get_storage_path`
Returns the path to the storage directory, creating it if it does not exist.

```python
from noesis_utils import get_storage_path

path = get_storage_path()
```