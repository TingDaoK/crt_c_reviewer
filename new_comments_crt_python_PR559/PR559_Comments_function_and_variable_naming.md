# PR #559 Code Review Comments - Function and Variable Naming

## Overview
This document contains detailed code review comments focused on function and variable naming conventions for CBOR bindings implementation in aws-crt-python PR #559.

## Comments by File

### awscrt/cbor.py

#### Line 11: Class Name Convention
**Line 11**: `class AwsCborType(IntEnum):`
- **Comment**: Class name follows correct `UpperCamelCase` convention. The `Aws` prefix is appropriate for AWS-specific classes.

#### Lines 32-33: Method Name Convention  
**Lines 32-33**: `def __init__(self):`
- **Comment**: Constructor follows Python naming conventions properly.

#### Lines 45-49: Method Name Convention
**Lines 45-49**: `def get_encoded_data(self) -> bytes:`
- **Comment**: Method name follows correct `snake_case()` convention. Descriptive and clear.

#### Lines 52-55: Method Name Convention
**Lines 52-55**: `def reset(self):`
- **Comment**: Method name follows correct `snake_case()` convention. Clear and concise.

#### Lines 57-74: Method Name Convention
**Lines 57-74**: `def write_int(self, val: int):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `val` is appropriately concise.

#### Line 68: Variable Naming Issue
**Line 68**: `val_to_encode = val`
- **Issue**: Variable name `val_to_encode` follows correct `snake_case` convention and is descriptive.

#### Lines 75-83: Method Name Convention
**Lines 75-83**: `def write_float(self, val: float):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 85-91: Method Name Convention
**Lines 85-91**: `def write_bytes(self, val: bytes):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 93-99: Method Name Convention
**Lines 93-99**: `def write_text(self, val: str):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 101-112: Method and Parameter Naming
**Lines 101-112**: `def write_array_start(self, number_entries: int):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `number_entries` is descriptive and follows `snake_case`.

#### Lines 114-125: Method and Parameter Naming  
**Lines 114-125**: `def write_map_start(self, number_entries: int):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `number_entries` is consistent with previous method.

#### Lines 127-136: Method and Parameter Naming
**Lines 127-136**: `def write_tag(self, tag_number: int):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `tag_number` is descriptive and follows `snake_case`.

#### Lines 138-141: Method Name Convention
**Lines 138-141**: `def write_null(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 143-146: Method Name Convention
**Lines 143-146**: `def write_undefined(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 148-151: Method Name Convention
**Lines 148-151**: `def write_indef_array_start(self):`
- **Comment**: Method name follows correct `snake_case()` convention. The abbreviation `indef` is consistent with CBOR terminology.

#### Lines 153-156: Method Name Convention
**Lines 153-156**: `def write_indef_map_start(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 158-162: Method Name Convention
**Lines 158-162**: `def write_indef_bytes_start(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 164-168: Method Name Convention
**Lines 164-168**: `def write_indef_text_start(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 170-174: Method Name Convention
**Lines 170-174**: `def write_break(self):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 176-179: Method Name Convention
**Lines 176-179**: `def write_bool(self, val: bool):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 181-189: Method Name Convention
**Lines 181-189**: `def write_epoch_time(self, val: float):`
- **Comment**: Method name follows correct `snake_case()` convention. Very descriptive for its purpose.

#### Lines 191-195: Method Name Convention
**Lines 191-195**: `def write_list(self, val: list):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 197-201: Method Name Convention
**Lines 197-201**: `def write_dict(self, val: dict):`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 203-221: Method Name Convention
**Lines 203-221**: `def write_data_item(self, data_item: Any):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `data_item` is descriptive and follows `snake_case`.

#### Line 233: Class Name Convention
**Line 233**: `class AwsCborDecoder(NativeResource):`
- **Comment**: Class name follows correct `UpperCamelCase` convention with appropriate `Aws` prefix.

#### Lines 242-254: Constructor Parameter Naming
**Lines 242-254**: `def __init__(self, src: bytes, on_epoch_time: Callable[[Union[int, float]], Any] = None, **kwargs):`
- **Comment**: Parameter names follow correct `snake_case` convention. `on_epoch_time` is descriptive and follows callback naming pattern.

#### Lines 256-260: Private Method Naming
**Lines 256-260**: `def _src = src`
- **Comment**: Private member variable `_src` correctly uses underscore prefix for private members.

#### Lines 262-266: Private Method Naming
**Lines 262-266**: `def _on_epoch_time_callback(self, epoch_secs: Union[int, float]) -> Any:`
- **Comment**: Private method name correctly uses underscore prefix. Parameter `epoch_secs` is descriptive and follows `snake_case`.

#### Lines 268-271: Method Name Convention
**Lines 268-271**: `def peek_next_type(self) -> AwsCborType:`
- **Comment**: Method name follows correct `snake_case()` convention and is very descriptive.

#### Lines 273-276: Method Name Convention
**Lines 273-276**: `def get_remaining_bytes_len(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention. Very descriptive.

#### Lines 278-282: Method Name Convention
**Lines 278-282**: `def get_remaining_bytes(self) -> bytes:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Line 284: Variable Naming Issue
**Line 284**: `remaining_length = _awscrt.cbor_decoder_get_remaining_bytes_len(self._binding)`
- **Comment**: Variable name `remaining_length` follows correct `snake_case` convention and is descriptive.

#### Lines 286-293: Method Name Convention
**Lines 286-293**: `def reset_src(self, src: bytes):`
- **Comment**: Method name follows correct `snake_case()` convention. Parameter name `src` is appropriately concise.

#### Lines 295-315: Method Name Convention
**Lines 295-315**: `def consume_next_single_element(self):`
- **Comment**: Method name follows correct `snake_case()` convention and is very descriptive of its function.

#### Lines 317-340: Method Name Convention
**Lines 317-340**: `def consume_next_whole_data_item(self):`
- **Comment**: Method name follows correct `snake_case()` convention and is very descriptive.

#### Lines 342-346: Method Name Convention
**Lines 342-346**: `def pop_next_unsigned_int(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention and clearly indicates the data type being returned.

#### Lines 348-353: Method Name Convention
**Lines 348-353**: `def pop_next_negative_int(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 355-359: Method Name Convention
**Lines 355-359**: `def pop_next_double(self) -> float:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 361-365: Method Name Convention
**Lines 361-365**: `def pop_next_bool(self) -> bool:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 367-371: Method Name Convention
**Lines 367-371**: `def pop_next_bytes(self) -> bytes:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 373-377: Method Name Convention
**Lines 373-377**: `def pop_next_text(self) -> str:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 379-388: Method Name Convention
**Lines 379-388**: `def pop_next_array_start(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention and is descriptive.

#### Lines 390-397: Method Name Convention
**Lines 390-397**: `def pop_next_map_start(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 399-406: Method Name Convention
**Lines 399-406**: `def pop_next_tag_val(self) -> int:`
- **Comment**: Method name follows correct `snake_case()` convention. The abbreviation `val` is consistent with CBOR terminology.

#### Lines 408-413: Method Name Convention
**Lines 408-413**: `def pop_next_list(self) -> list:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 415-420: Method Name Convention
**Lines 415-420**: `def pop_next_map(self) -> dict:`
- **Comment**: Method name follows correct `snake_case()` convention.

#### Lines 422-447: Method Name Convention
**Lines 422-447**: `def pop_next_data_item(self) -> Any:`
- **Comment**: Method name follows correct `snake_case()` convention and is very descriptive of its generic functionality.

### source/cbor.c

#### Line 13: Static Variable Naming
**Line 13**: `static const char *s_capsule_name_cbor_encoder = "aws_cbor_encoder";`
- **Comment**: Static variable name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 15: Function Naming
**Line 15**: `static struct aws_cbor_encoder *s_cbor_encoder_from_capsule(PyObject *py_capsule)`
- **Comment**: Static function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 19: Function Naming
**Line 19**: `static void s_cbor_encoder_capsule_destructor(PyObject *py_capsule)`
- **Comment**: Static function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 24: Function Naming
**Line 24**: `PyObject *aws_py_cbor_encoder_new(PyObject *self, PyObject *args)`
- **Comment**: Function name follows correct convention with `aws_py_` prefix for Python bindings and `snake_case`. Very descriptive.

#### Line 32: Function Naming
**Line 32**: `PyObject *aws_py_cbor_encoder_get_encoded_data(PyObject *self, PyObject *args)`
- **Comment**: Function name follows correct convention with `aws_py_` prefix for Python bindings and `snake_case`. Very descriptive.

#### Line 41: Variable Naming
**Line 41**: `struct aws_byte_cursor encoded_data = aws_cbor_encoder_get_encoded_data(encoder);`
- **Comment**: Variable name `encoded_data` follows correct `snake_case` convention and is descriptive.

#### Lines 48-53: Macro Naming
**Lines 48-53**: `#define S_ENCODER_WRITE_PYOBJECT(ctype, py_conversion, field)`
- **Comment**: Macro name follows correct convention with `S_` prefix for static/internal macros and `ALL_CAPS`. Very descriptive.

#### Lines 55-61: Generated Function Naming
**Lines 55-61**: Generated functions like `s_cbor_encoder_write_pyobject_as_uint`
- **Comment**: Generated function names follow correct convention with `s_` prefix for statics and `snake_case`. Very descriptive and consistent.

#### Line 63: Function Naming
**Line 63**: `static PyObject *s_cbor_encoder_write_pyobject(struct aws_cbor_encoder *encoder, PyObject *py_object);`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 65: Function Naming
**Line 65**: `static PyObject *s_cbor_encoder_write_pylong(struct aws_cbor_encoder *encoder, PyObject *py_object)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 67: Variable Naming
**Line 67**: `long val = 0;`
- **Comment**: Variable name `val` is appropriately concise for this context.

#### Line 68: Variable Naming
**Line 68**: `int overflow = 0;`
- **Comment**: Variable name `overflow` is descriptive and follows `snake_case`.

#### Line 70: Variable Naming
**Line 70**: `val = PyLong_AsLongAndOverflow(py_object, &overflow);`
- **Comment**: Using existing variable `val` appropriately.

#### Lines 77-79: Variable Naming
**Lines 77-79**: `PyObject *abs_val = PyNumber_Negative(py_object);`
- **Comment**: Variable name `abs_val` is descriptive and follows `snake_case`.

#### Line 83: Variable Naming
**Line 83**: `PyObject *minus_one = PyLong_FromLong(1);`
- **Comment**: Variable name `minus_one` is very descriptive and follows `snake_case`.

#### Line 88: Variable Naming
**Line 88**: `PyObject *result = PyNumber_Subtract(abs_val, minus_one);`
- **Comment**: Variable name `result` is appropriate for this context.

#### Line 95: Variable Naming
**Line 95**: `uint64_t val_to_encode = PyLong_AsUnsignedLongLong(result);`
- **Comment**: Variable name `val_to_encode` is very descriptive and follows `snake_case`.

#### Line 104: Variable Naming
**Line 104**: `uint64_t val_to_encode = PyLong_AsUnsignedLongLong(py_object);`
- **Comment**: Variable name `val_to_encode` is consistent with previous usage and descriptive.

#### Line 115: Function Naming
**Line 115**: `static PyObject *s_cbor_encoder_write_pylist(struct aws_cbor_encoder *encoder, PyObject *py_list)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 133: Function Naming
**Line 133**: `static PyObject *s_cbor_encoder_write_pydict(struct aws_cbor_encoder *encoder, PyObject *py_dict)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Lines 194-200: Macro Naming
**Lines 194-200**: `#define ENCODER_WRITE(field, encoder_fn)`
- **Comment**: Macro name follows correct convention with `ALL_CAPS`. Very descriptive.

#### Line 216: Function Naming
**Line 216**: `PyObject *aws_py_cbor_encoder_write_simple_types(PyObject *self, PyObject *args)`
- **Comment**: Function name follows correct convention with `aws_py_` prefix for Python bindings and `snake_case`. Very descriptive.

#### Line 220: Variable Naming
**Line 220**: `Py_ssize_t type_enum = AWS_CBOR_TYPE_UNKNOWN;`
- **Comment**: Variable name `type_enum` is descriptive and follows `snake_case`.

#### Line 248: Struct Naming
**Line 248**: `struct decoder_binding {`
- **Comment**: Struct name follows correct `snake_case` convention.

#### Line 252: Member Variable Naming
**Line 252**: `PyObject *self_py;`
- **Comment**: Member variable name follows correct `snake_case` convention with descriptive suffix.

#### Line 255: Static Variable Naming
**Line 255**: `static const char *s_capsule_name_cbor_decoder = "aws_cbor_decoder";`
- **Comment**: Static variable name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 257: Function Naming
**Line 257**: `static struct aws_cbor_decoder *s_cbor_decoder_from_capsule(PyObject *py_capsule)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 264: Function Naming
**Line 264**: `static void s_cbor_decoder_capsule_destructor(PyObject *py_capsule)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 270: Function Naming
**Line 270**: `PyObject *aws_py_cbor_decoder_new(PyObject *self, PyObject *args)`
- **Comment**: Function name follows correct convention with `aws_py_` prefix for Python bindings and `snake_case`. Very descriptive.

#### Line 274: Variable Naming
**Line 274**: `PyObject *py_self = NULL;`
- **Comment**: Variable name `py_self` is descriptive with appropriate prefix and follows `snake_case`.

#### Line 280: Variable Naming
**Line 280**: `struct decoder_binding *binding = aws_mem_calloc(...);`
- **Comment**: Variable name `binding` is appropriately concise for this context.

#### Line 289: Function Naming
**Line 289**: `static struct aws_cbor_decoder *s_get_decoder_from_py_arg(PyObject *self, PyObject *args)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Lines 297-302: Macro Naming
**Lines 297-302**: `#define S_POP_NEXT_TO_PYOBJECT(ctype, field, py_conversion)`
- **Comment**: Macro name follows correct convention with `S_` prefix for static/internal macros and `ALL_CAPS`. Very descriptive.

#### Lines 308-314: Macro Naming
**Lines 308-314**: `#define S_POP_NEXT_TO_PYOBJECT_CURSOR(field, py_conversion)`
- **Comment**: Macro name follows correct convention with `S_` prefix for static/internal macros and `ALL_CAPS`. Very descriptive.

#### Line 325: Function Naming
**Line 325**: `static PyObject *s_cbor_decoder_pop_next_data_item_to_pyobject(struct decoder_binding *binding);`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 330: Function Naming
**Line 330**: `static PyObject *s_cbor_decoder_pop_next_data_item_to_py_list(struct decoder_binding *binding)`
- **Comment**: Function name follows correct convention with `s_` prefix for statics and `snake_case`. Very descriptive.

#### Line 332: Variable Naming
**Line 332**: `struct aws_cbor_decoder *decoder = binding->native;`
- **Comment**: Variable name `decoder` is appropriately concise for this context.

#### Line 333: Variable Naming
**Line 333**: `enum aws_cbor_type out_type = AWS_CBOR_TYPE_UNKNOWN;`
- **Comment**: Variable name `out_type` is descriptive and follows `snake_case`.

#### Line 338: Variable Naming
**Line 338**: `uint64_t num_array_item = 0;`
- **Comment**: Variable name `num_array_item` is descriptive and follows `snake_case`.

### source/cbor.h

#### Line 1: Header Guard Naming
**Line 1**: `#ifndef AWS_CRT_PYTHON_CBOR_H`
- **Comment**: Header guard follows correct convention with `ALL_CAPS` and descriptive path-based naming.

#### Lines 13-56: Function Declaration Naming
**Lines 13-56**: All function declarations like `aws_py_cbor_encoder_new`, `aws_py_cbor_encoder_get_encoded_data`, etc.
- **Comment**: All function names follow correct convention with `aws_py_` prefix for Python bindings and `snake_case`. Very descriptive and consistent.

## Summary

### Strengths:
1. **Consistent Naming**: All functions, variables, and classes follow the established AWS CRT Python naming conventions
2. **Descriptive Names**: Function and variable names clearly indicate their purpose
3. **Proper Prefixes**: Private members use underscore prefix, static functions use `s_` prefix, Python bindings use `aws_py_` prefix
4. **Type Consistency**: Similar functions have consistent naming patterns (e.g., all `write_*` methods, all `pop_next_*` methods)

### Minor Observations:
1. **Abbreviations**: The use of `indef` for "indefinite" and `val` for "value" is consistent with CBOR terminology and appropriately concise
2. **Parameter Names**: Parameter names like `epoch_secs`, `tag_number`, `number_entries` are descriptive and follow `snake_case`
3. **Callback Naming**: The callback function `_on_epoch_time_callback` follows the private method naming convention properly

### Overall Assessment:
The naming conventions in this PR are excellent and fully conform to the established AWS CRT Python coding standards. The code demonstrates strong consistency in naming patterns across both Python and C components.