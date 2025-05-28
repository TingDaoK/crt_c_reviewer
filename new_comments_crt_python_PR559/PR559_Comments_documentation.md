# PR 559 CBOR Bindings - Detailed Documentation Review Comments

This PR introduces CBOR (Concise Binary Object Representation) encoding and decoding capabilities to aws-crt-python. Based on the analysis of the code and knowledge base, here are comprehensive documentation-focused comments:

## Python Module (awscrt/cbor.py) Documentation Issues

### Line 12-28: AwsCborType enum documentation
**Line 12**: The comment about corresponding to `enum aws_cbor_type` in aws/common/cbor.h is good, but the documentation could be enhanced.

```suggestion
class AwsCborType(IntEnum):
    """CBOR data type enumeration.
    
    Corresponds to `enum aws_cbor_type` in aws/common/cbor.h from AWS C Common Runtime.
    These values represent the different types of data items that can be encoded/decoded in CBOR format
    according to RFC 8949.
    
    Attributes:
        Unknown: Unknown/uninitialized type
        UnsignedInt: Unsigned integer (major type 0)
        NegativeInt: Negative integer (major type 1) 
        Float: Floating-point number (major type 7)
        Bytes: Byte string (major type 2)
        Text: Text string (major type 3)
        ArrayStart: Start of definite-length array (major type 4)
        MapStart: Start of definite-length map (major type 5)
        Tag: Semantic tag (major type 6)
        Bool: Boolean value (major type 7, simple value)
        Null: Null value (major type 7, simple value 22)
        Undefined: Undefined value (major type 7, simple value 23)
        Break: Break stop code for indefinite-length items (major type 7, simple value 31)
        IndefBytes: Start of indefinite-length byte string
        IndefStr: Start of indefinite-length text string
        IndefArray: Start of indefinite-length array
        IndefMap: Start of indefinite-length map
    """
```

### Line 30-38: AwsCborEncoder class documentation
**Line 30**: The class docstring is adequate but could provide more comprehensive usage guidance and thread safety information.

```suggestion
class AwsCborEncoder(NativeResource):
    """CBOR encoder for converting Python objects to CBOR binary format.
    
    This class provides methods to encode various Python data types into CBOR (Concise Binary Object 
    Representation) format as defined in RFC 8949. The encoder builds CBOR data incrementally by 
    calling write_* methods in sequence.
    
    Thread Safety:
        This class is NOT thread-safe. Each encoder instance should only be used from a single thread.
        Create separate encoder instances for concurrent encoding operations.
    
    Memory Management:
        The encoder automatically manages internal memory and integrates with AWS CRT memory management.
        Call reset() to clear internal buffers for reuse, or let the encoder be garbage collected.
    
    Typical Usage:
        ```python
        encoder = AwsCborEncoder()
        encoder.write_int(42)
        encoder.write_text("hello")
        encoder.write_array_start(2)
        encoder.write_bool(True)
        encoder.write_null()
        cbor_data = encoder.get_encoded_data()
        ```
    
    For complex data structures, use write_data_item() which automatically handles nested objects:
        ```python
        encoder = AwsCborEncoder()
        data = {"numbers": [1, 2, 3], "text": "example", "flag": True}
        encoder.write_data_item(data)
        cbor_data = encoder.get_encoded_data()
        ```
    """
```

### Line 47-51: get_encoded_data method documentation
**Line 47**: The return type and behavior documentation needs clarification about empty state handling.

```suggestion
def get_encoded_data(self) -> bytes:
    """Return the current encoded data as bytes.
    
    This method returns all CBOR data that has been written to the encoder since
    creation or the last reset() call. The returned bytes represent valid CBOR
    data that can be decoded by any CBOR-compliant decoder.
    
    Returns:
        bytes: The complete CBOR-encoded data. Returns empty bytes (b'') if no data
               has been written yet, rather than None.
    
    Note:
        This method does not modify the encoder state. You can call it multiple times
        to get the current encoded data, then continue writing more data.
    """
```

### Line 53-55: reset method documentation
**Line 53**: The reset method documentation should clarify the behavior more thoroughly.

```suggestion
def reset(self):
    """Clear the encoder's internal buffer and reset to initial state.
    
    After calling this method, the encoder is ready to encode new data from scratch.
    Any previously encoded data is discarded and cannot be recovered.
    
    This is useful for reusing the same encoder instance to encode multiple
    independent CBOR documents without creating new encoder objects.
    
    Note:
        This operation does not raise exceptions and always succeeds.
    """
```

### Line 57-69: write_int method documentation
**Line 57**: The integer encoding documentation has several issues that need clarification.

```suggestion
def write_int(self, val: int):
    """Write an integer value in CBOR format.
    
    This method automatically determines the appropriate CBOR encoding based on the
    integer's value and sign:
    - Non-negative integers (0 to 2^64-1): Encoded as CBOR unsigned integers (major type 0)
    - Negative integers (-1 to -2^64): Encoded as CBOR negative integers (major type 1)
    - Integers outside the 64-bit range: Currently raise OverflowError
    
    CBOR negative integers are encoded as (-1 - n) where n is the absolute value minus 1.
    For example, -1 is encoded as 0, -2 as 1, etc.
    
    Args:
        val (int): Integer value to encode. Must be within the range that can be
                  represented in CBOR format.
    
    Raises:
        OverflowError: If the integer is too large to be represented in CBOR format.
                      Currently, bignum support (RFC 8949 section 3.4.3) is not implemented.
        TypeError: If val is not an integer type.
    
    Note:
        Python's arbitrary precision integers are supported up to 64-bit range.
        Future versions may add support for CBOR bignums (tags 2 and 3) for larger integers.
    """
```

### Line 78-84: write_float method documentation
**Line 78**: The float encoding behavior needs better documentation about precision handling.

```suggestion
def write_float(self, val: float):
    """Write a floating-point number in CBOR format.
    
    Encodes the float using the most compact CBOR representation possible without
    loss of precision. The underlying C implementation may choose between half-precision
    (16-bit), single-precision (32-bit), or double-precision (64-bit) encoding based
    on the value's requirements.
    
    Special float values are properly handled:
    - Positive/negative infinity
    - NaN (Not a Number)  
    - Positive/negative zero
    
    Args:
        val (float): Floating-point value to encode.
    
    Raises:
        TypeError: If val cannot be converted to a float.
    
    Note:
        If the float value can be exactly represented as an integer without loss
        of precision, it may be encoded as a CBOR integer instead of a float for
        more compact representation.
    """
```

### Line 95-105: write_array_start method documentation  
**Line 95**: The array_start method has validation logic that should be documented properly.

```suggestion
def write_array_start(self, number_entries: int):
    """Begin encoding a definite-length CBOR array.
    
    This method writes the array header that specifies exactly how many data items
    will follow as array elements. After calling this method, you must write exactly
    `number_entries` data items using other write_* methods.
    
    For indefinite-length arrays, use write_indef_array_start() instead.
    
    Args:
        number_entries (int): The exact number of data items that will be written
                             as array elements. Must be in range [0, 2^64-1].
    
    Raises:
        OverflowError: If number_entries is negative or exceeds 2^64-1.
        
    Example:
        ```python
        encoder.write_array_start(3)
        encoder.write_int(1)
        encoder.write_text("hello") 
        encoder.write_bool(True)
        # Array is now complete with exactly 3 elements
        ```
    
    Warning:
        Writing fewer or more than `number_entries` data items will result in
        invalid CBOR data that cannot be properly decoded.
    """
```

### Line 107-117: write_map_start method documentation
**Line 107**: The map_start method has an inconsistent exception type (ValueError vs OverflowError).

```suggestion
def write_map_start(self, number_entries: int):
    """Begin encoding a definite-length CBOR map.
    
    This method writes the map header that specifies exactly how many key-value pairs
    will follow. After calling this method, you must write exactly `number_entries * 2`
    data items in alternating key-value order.
    
    Args:
        number_entries (int): The exact number of key-value pairs that will be written.
                             Must be in range [0, 2^64-1].
    
    Raises:
        OverflowError: If number_entries is negative or exceeds 2^64-1.
        
    Example:
        ```python
        encoder.write_map_start(2)
        encoder.write_text("name")     # First key
        encoder.write_text("Alice")    # First value  
        encoder.write_text("age")      # Second key
        encoder.write_int(30)          # Second value
        # Map is now complete with exactly 2 key-value pairs
        ```
    
    Warning:
        Writing an incorrect number of key-value pairs will result in invalid CBOR data.
        Keys and values can be any CBOR data type, including nested arrays and maps.
    """
```

### Line 119-127: write_tag method documentation
**Line 119**: The tag documentation needs more comprehensive information about CBOR tags.

```suggestion
def write_tag(self, tag_number: int):
    """Write a CBOR semantic tag.
    
    Tags provide additional semantic information about the data item that follows.
    The tag applies to the next single data item written to the encoder.
    
    Common standardized tags include:
    - 0: Standard date/time string (RFC 3339)
    - 1: Epoch-based date/time (seconds since Unix epoch)
    - 2: Positive bignum (byte string)
    - 3: Negative bignum (byte string)
    - 21-23: Base64/Base16 encoded strings
    
    Args:
        tag_number (int): The tag number as defined in RFC 8949 or IANA registry.
                         Must be in range [0, 2^64-1].
    
    Raises:
        ValueError: If tag_number is negative or exceeds 2^64-1.
    
    Example:
        ```python
        encoder.write_tag(1)  # Epoch time tag
        encoder.write_float(1640995200.0)  # Unix timestamp
        ```
    
    Note:
        The user is responsible for ensuring the tagged value conforms to the
        tag's semantic requirements as specified in RFC 8949 section 3.4.
        Invalid tag-value combinations may cause decoding issues.
    """
```

### Line 169-175: write_epoch_time method documentation
**Line 169**: This helper method needs clearer documentation about its specific behavior.

```suggestion
def write_epoch_time(self, val: float):
    """Write a Unix epoch timestamp with CBOR semantic tag 1.
    
    This is a convenience method that automatically applies the standard CBOR
    epoch time tag (tag 1) and encodes the timestamp value. The timestamp
    represents seconds since the Unix epoch (1970-01-01 00:00:00 UTC).
    
    The value is encoded using the most compact representation possible without
    loss of precision (integer if no fractional seconds, float otherwise).
    
    Args:
        val (float): Seconds since Unix epoch. Can include fractional seconds
                    for sub-second precision.
    
    Example:
        ```python
        import time
        encoder.write_epoch_time(time.time())  # Current timestamp
        encoder.write_epoch_time(1640995200.0)  # Specific timestamp
        encoder.write_epoch_time(1640995200.5)  # With 500ms precision
        ```
    
    Note:
        This method is equivalent to calling write_tag(1) followed by write_float(val),
        but provides a more semantic API for timestamp encoding.
    """
```

### Line 215-242: write_data_item method documentation
**Line 215**: This generic method needs comprehensive documentation about type mapping and error handling.

```suggestion
def write_data_item(self, data_item: Any):
    """Encode a Python object as CBOR using automatic type detection.
    
    This method recursively encodes Python objects to their corresponding CBOR
    representations. It's the most convenient way to encode complex nested data
    structures.
    
    Type Mapping:
        - int → CBOR unsigned/negative integer
        - float → CBOR floating-point number  
        - bool → CBOR boolean (true/false)
        - bytes → CBOR byte string
        - str → CBOR text string
        - list → CBOR definite-length array (recursive encoding of elements)
        - dict → CBOR definite-length map (recursive encoding of key-value pairs)
        - None → CBOR null value
    
    Args:
        data_item (Any): Python object to encode. Must be one of the supported types
                        or contain only supported types if it's a container.
    
    Raises:
        ValueError: If data_item contains unsupported types that cannot be converted
                   to CBOR format.
        OverflowError: If integer values exceed CBOR's representable range.
        TypeError: If the object type is not supported for CBOR encoding.
        
    Example:
        ```python
        data = {
            "name": "Alice",
            "age": 30,
            "scores": [95, 87, 92],
            "active": True,
            "metadata": None
        }
        encoder.write_data_item(data)
        ```
    
    Performance Note:
        For simple types, using specific write_* methods may be more efficient
        than the generic write_data_item() method.
    """
```

## AwsCborDecoder Class Documentation

### Line 244-255: AwsCborDecoder class documentation
**Line 244**: The decoder class documentation needs enhancement similar to the encoder.

```suggestion
class AwsCborDecoder(NativeResource):
    """CBOR decoder for converting CBOR binary data to Python objects.
    
    This class provides methods to decode CBOR (Concise Binary Object Representation) 
    binary data into Python objects. The decoder processes CBOR data incrementally,
    allowing fine-grained control over the decoding process.
    
    Thread Safety:
        This class is NOT thread-safe. Each decoder instance should only be used 
        from a single thread.
    
    Memory Management:
        The decoder holds a reference to the source bytes to avoid copying large
        amounts of data. The source bytes must remain valid for the decoder's lifetime.
    
    Typical Usage:
        ```python
        cbor_data = b'\\xa2\\x64name\\x65Alice\\x63age\\x18\\x1e'
        decoder = AwsCborDecoder(cbor_data)
        
        # Peek at the next data type
        if decoder.peek_next_type() == AwsCborType.MapStart:
            result = decoder.pop_next_map()
            print(result)  # {'name': 'Alice', 'age': 30}
        ```
    
    Advanced Usage with Manual Decoding:
        ```python
        decoder = AwsCborDecoder(cbor_data)
        while decoder.get_remaining_bytes_len() > 0:
            data_type = decoder.peek_next_type()
            if data_type == AwsCborType.UnsignedInt:
                value = decoder.pop_next_unsigned_int()
            elif data_type == AwsCborType.Text:
                value = decoder.pop_next_text()
            # ... handle other types
        ```
    """
```

### Line 257-275: AwsCborDecoder.__init__ documentation
**Line 257**: The constructor documentation has a type annotation error and needs clarification.

```suggestion
def __init__(self, src: bytes, on_epoch_time: Callable[[Union[int, float]], Any] = None, **kwargs):
    """Create a CBOR decoder instance.
    
    Args:
        src (bytes): The CBOR-encoded binary data to decode. This data is not copied,
                    so it must remain valid for the decoder's lifetime.
        on_epoch_time (Callable[[Union[int, float]], Any], optional): 
            Callback function invoked when CBOR tag 1 (epoch time) is encountered
            during decoding. The callback receives the numeric timestamp value
            and should return the desired Python representation.
            
            Callback signature:
                def callback(epoch_secs: Union[int, float]) -> Any:
                    # epoch_secs: seconds since Unix epoch
                    # return: any Python object representing the timestamp
                    
        **kwargs: Reserved for future expansion. Currently unused.
    
    Example:
        ```python
        import datetime
        
        def timestamp_to_datetime(epoch_secs):
            return datetime.datetime.fromtimestamp(epoch_secs)
            
        decoder = AwsCborDecoder(cbor_data, on_epoch_time=timestamp_to_datetime)
        ```
    
    Note:
        If on_epoch_time is not provided, epoch timestamps are returned as their
        numeric values (int or float) without conversion.
    """
```

### Line 284-286: peek_next_type method documentation
**Line 284**: Simple methods still benefit from more detailed documentation.

```suggestion
def peek_next_type(self) -> AwsCborType:
    """Determine the type of the next CBOR data item without consuming it.
    
    This method examines the next CBOR data item in the stream and returns its
    type without advancing the decoder's position. This allows for conditional
    decoding logic based on the upcoming data type.
    
    Returns:
        AwsCborType: The type of the next data item in the CBOR stream.
    
    Raises:
        RuntimeError: If the CBOR data is malformed or truncated.
        
    Example:
        ```python
        next_type = decoder.peek_next_type()
        if next_type == AwsCborType.MapStart:
            my_dict = decoder.pop_next_map()
        elif next_type == AwsCborType.ArrayStart:
            my_list = decoder.pop_next_list()
        ```
    
    Note:
        This method can be called multiple times without changing the decoder state.
        It's essential for implementing conditional decoding logic.
    """
```

### Line 298-302: get_remaining_bytes method documentation
**Line 298**: This method has a potential bug in its implementation that needs documentation.

```suggestion
def get_remaining_bytes(self) -> bytes:
    """Return the remaining unprocessed CBOR data as bytes.
    
    This method returns a slice of the original source data that has not yet been
    consumed by the decoder. Useful for debugging, validation, or passing remaining
    data to another decoder instance.
    
    Returns:
        bytes: The remaining unprocessed CBOR data. Returns empty bytes (b'') if
               all data has been consumed.
    
    Implementation Note:
        This method calculates the remaining data by slicing from the end of the
        original source bytes. The slice size is determined by get_remaining_bytes_len().
        
    Example:
        ```python
        decoder = AwsCborDecoder(cbor_data)
        first_item = decoder.pop_next_data_item()
        remaining = decoder.get_remaining_bytes()  # Data for additional items
        ```
    
    Warning:
        The returned bytes share memory with the original source data. Modifications
        to the source data after decoder creation may affect the returned bytes.
    """
```

### Line 310-334: consume_next_single_element method documentation
**Line 310**: This method has excellent example documentation but needs some clarification about its purpose.

```suggestion
def consume_next_single_element(self):
    """Consume only the next CBOR element header without processing its content.
    
    This method advances the decoder past the next single CBOR element without
    decoding its value or any nested content. It's primarily useful for:
    - Skipping over unwanted data items
    - Manual handling of indefinite-length containers
    - Low-level CBOR stream processing
    
    The method only consumes the element's header/marker, not its payload:
    - For primitives (int, float, bool): Consumes the complete item
    - For containers (arrays, maps): Only consumes the start marker
    - For indefinite-length items: Only consumes the start marker, not until break
    
    Example with indefinite-length map:
        CBOR data: 0xbf6346756ef563416d7421ff
        BF         -- Start indefinite-length map (CONSUMED)
        63         -- First key, UTF-8 string length 3 (NOT CONSUMED)
            46756e --   \"Fun\"
        F5         -- First value, true  
        63         -- Second key, UTF-8 string length 3
            416d74 --   \"Amt\"
        21         -- Second value, -2
        FF         -- \"break\"
        
    After calling this method, the next element to decode starts from 0x63.
    
    Raises:
        RuntimeError: If the CBOR data is malformed or if there are no more elements.
    
    See Also:
        consume_next_whole_data_item(): Consumes an entire data item including content.
    """
```

### Line 421-433: pop_next_array_start method documentation
**Line 421**: This method has good documentation about indefinite-length handling but could be clearer.

```suggestion
def pop_next_array_start(self) -> int:
    """Decode and consume a definite-length array start marker.
    
    This method is for manual, low-level array processing. It only processes the
    array header and returns the number of elements, but does not decode the
    array elements themselves.
    
    Returns:
        int: The number of data items that follow as array elements.
    
    Raises:
        ValueError: If the next item is not a definite-length array start marker.
        RuntimeError: If the CBOR data is malformed.
    
    Usage Pattern:
        ```python
        if decoder.peek_next_type() == AwsCborType.ArrayStart:
            count = decoder.pop_next_array_start()
            elements = []
            for i in range(count):
                elements.append(decoder.pop_next_data_item())
        ```
    
    Indefinite-Length Arrays:
        For indefinite-length arrays (AwsCborType.IndefArray), use this pattern:
        ```python
        if decoder.peek_next_type() == AwsCborType.IndefArray:
            decoder.consume_next_single_element()  # Skip start marker
            elements = []
            while decoder.peek_next_type() != AwsCborType.Break:
                elements.append(decoder.pop_next_data_item())
            decoder.consume_next_single_element()  # Consume break marker
        ```
    
    Note:
        For most use cases, pop_next_list() is more convenient as it handles
        both definite and indefinite-length arrays automatically.
    """
```

## C Source File (source/cbor.c) Documentation Issues

### Line 45-50: get_encoded_data TODO comment
**Line 45**: There's a TODO comment about returning empty bytes vs None that should be addressed.

```c
// TODO: probably better to be empty instead of None??
if (encoded_data.len == 0) {
    Py_RETURN_NONE;
}
```

**Important Documentation Issue**: This behavior is inconsistent with the Python documentation. The Python method documents returning empty bytes, but the C implementation returns None for empty data. This should be documented as a known inconsistency or fixed.

### Line 133-150: Integer overflow handling  
**Line 133**: The big integer overflow handling needs better documentation in the error messages.

The current error message "The integer is too large, BigNumber is not supported yet." should be more descriptive about the limitations and future plans.

### Line 280-300: Memory management in decoder binding
**Line 280**: The decoder binding structure and memory management needs documentation comments explaining the lifetime relationship between the Python object and C structures.

## Test File Documentation

The test file `test/test_cbor.py` has good coverage but some test methods need better documentation:

### Line 13-40: test_cbor_encode_decode_int method
The integer encoding test should document the specific test cases and their significance for edge cases.

### Line 177-215: Type conversion test methods
The `_convert_expect` method and related test infrastructure should have comprehensive documentation explaining the test data format and conversion logic.

## General Documentation Improvements Needed

1. **Thread Safety**: All classes need explicit thread safety documentation
2. **Memory Management**: Document the relationship between Python objects and C memory management  
3. **Error Handling**: Standardize error types and messages across methods
4. **Performance Notes**: Add guidance about when to use specific methods vs generic methods
5. **RFC Compliance**: Document which parts of RFC 8949 are supported vs planned
6. **Cross-Platform Behavior**: Document any platform-specific behavior differences

## Critical Issues for Documentation

1. **Line 107-117**: Inconsistent exception types (ValueError vs OverflowError) between similar methods
2. **Line 45**: Mismatch between documented behavior (empty bytes) and actual behavior (None) 
3. **Line 298**: Potential slice calculation issue in `get_remaining_bytes()` implementation
4. **Missing reset_src documentation**: The decoder's `reset_src` method needs comprehensive documentation about data lifetime and memory implications