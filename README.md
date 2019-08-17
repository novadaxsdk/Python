# NovaDAX Python SDK

### Installation

*The SDK is compiled by Python 3.6 and above*

To install by source code, run below command

```shell
pip3 install novadax
```

### Quick Start

In your python project, you can follow below steps:

* Create the client instance.
* Call the interfaces provided by client.

```python
from novadax import RequestClient as NovaClient

nova_client = NovaClient('your access key(optional)', 'your secret key(optional)')

result = nova_client.get_timestamp()
print(result)
```

### More information

Please see our [API documentation website](https://doc.novadax.com/en-US/).