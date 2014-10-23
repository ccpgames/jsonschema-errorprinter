=======================
jsonschema-errorprinter
=======================

Validation Error Pretty-Printer for the [jsonschema](https://github.com/Julian/jsonschema) library.

The `check_json` function wraps ` validate()` and in case of ValidationError exception, returns a string containing a pretty printed error report.

Example:
```python
>>> from jsonschemaerror import check_json

>>> # A sample schema, like what we'd get from json.load()
>>> schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }

>>> # If check_json returns None, no exception was raised by validate():
>>>  print check_json({"name" : "Eggs", "price" : 34.99}, schema)
None

>>> print check_json({"name" : "Eggs", "price" : "Invalid"}, schema)
Schema check failed for '?'
Error in line 2:
   1:    {
   2: >>>    "price": "Invalid",
   3:        "name": "Eggs"
   4:    }

'Invalid' is not of type 'number'

Failed validating 'type' in schema['properties']['price']:
    {'type': 'number'}

On instance['price']:
    'Invalid'
```



