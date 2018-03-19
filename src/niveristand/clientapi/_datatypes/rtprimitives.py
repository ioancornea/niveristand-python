import sys
from niveristand import _internal
from NationalInstruments.VeriStand.Data import BooleanValue as ClientApiBooleanValue  # noqa: E501, I100 We need these C# imports to be out of order.
from NationalInstruments.VeriStand.Data import BooleanValueArray as ClientApiBooleanValueArray
from NationalInstruments.VeriStand.Data import DataValue
from NationalInstruments.VeriStand.Data import DoubleValue as ClientApiDoubleValue
from NationalInstruments.VeriStand.Data import DoubleValueArray as ClientApiDoubleValueArray
from NationalInstruments.VeriStand.Data import I32Value as ClientApiI32Value
from NationalInstruments.VeriStand.Data import I32ValueArray as ClientApiI32ValueArray
from NationalInstruments.VeriStand.Data import I64Value as ClientApiI64Value
from NationalInstruments.VeriStand.Data import I64ValueArray as ClientApiI64ValueArray
from NationalInstruments.VeriStand.Data import U32Value as ClientApiU32Value
from NationalInstruments.VeriStand.Data import U32ValueArray as ClientApiU32ValueArray
from NationalInstruments.VeriStand.Data import U64Value as ClientApiU64Value
from NationalInstruments.VeriStand.Data import U64ValueArray as ClientApiU64ValueArray
from niveristand import _errormessages
from niveristand import errors as nivsexceptions
from niveristand.clientapi import realtimesequencedefinition
from System import Int32 as SystemInt32
from System import Int64 as SystemInt64
from System import UInt32 as SystemUInt32
from System import UInt64 as SystemUInt64

_internal.dummy()


def get_class_by_name(name):
    return VALID_TYPES[name]


def is_supported_data_type(name):
    return name in VALID_TYPES


def is_supported_return_type(name):
    return name in VALID_RETURN_TYPES


def is_scalar_type(name):
    return name in VALID_RETURN_TYPES


def is_channel_ref_type(name):
    return name in CHANNEL_REF_TYPES


class DataType(object):
    def __init__(self, value, description="", units=""):
        if isinstance(value, DataValue):
            self._data_value = value
        elif isinstance(value, DataType):
            self._data_value = self._to_data_value(value.value)
        else:
            self._data_value = self._to_data_value(value)

    def __str__(self):
        return str(self._data_value)

    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(_errormessages.invalid_type_to_convert)

    @staticmethod
    def _is_compatible_with_datatype(other):
        return isinstance(other, (int, float)) or (sys.version_info < (2, 8) and isinstance(other, long))  # noqa F821

    @staticmethod
    def _is_integer_type(other):
        return isinstance(other, int) or (sys.version_info < (2, 8) and isinstance(other, long))  # noqa F821

    @staticmethod
    def _is_valid_assign_type(other):
        return isinstance(other, (int, float, bool)) or (sys.version_info < (2, 8) and isinstance(other, long))  # noqa F821

    def __add__(self, other):
        if isinstance(other, DataType):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DataType):
            return self.value - other.value
        elif isinstance(other, (int, float)):
            return self.value - other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rsub__(self, other):
        if isinstance(other, DataType):
            return other.value - self.value
        elif isinstance(other, (int, float)):
            return other - self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __mul__(self, other):
        if isinstance(other, DataType):
            return self.value * other.value
        elif isinstance(other, (int, float)):
            return self.value * other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rdivmod__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __floordiv__(self, other):
        if isinstance(other, DataType):
            return self.value // other.value
        elif isinstance(other, (int, float)):
            return self.value // other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rfloordiv__(self, other):
        if isinstance(other, DataType):
            return other.value // self.value
        elif isinstance(other, (int, float)):
            return other // self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __truediv__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rtruediv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __div__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rdiv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value

    def __pow__(self, power, modulo=None):
        if isinstance(power, DataType):
            return self.value ** power.value
        elif isinstance(power, (int, float)):
            return self.value ** power
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rpow__(self, other):
        if isinstance(other, DataType):
            return other.value ** self.value
        elif isinstance(other, (int, float)):
            return other ** self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __mod__(self, other):
        if isinstance(other, DataType):
            return self.value % other.value
        elif self._is_compatible_with_datatype(other):
            return self.value % other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rmod__(self, other):
        if isinstance(other, DataType):
            return other.value % self.value
        elif self._is_compatible_with_datatype(other):
            return other % self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __and__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value & other.value
        elif self._is_integer_type(other):
            return self.value & other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value | other.value
        elif self._is_integer_type(other):
            return self.value | other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ror__(self, other):
        return self.__or__(other)

    def __xor__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value ^ other.value
        elif self._is_integer_type(other):
            return self.value ^ other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rxor__(self, other):
        return self.__xor__(other)

    def __lshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value << other.value
        elif self._is_integer_type(other):
            return self.value << other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rlshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return other.value << self.value
        elif self._is_integer_type(other):
            return other << self.value

        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value >> other.value
        elif self._is_integer_type(other):
            return self.value >> other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rrshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return other.value >> self.value
        elif self._is_integer_type(other):
            return other >> self.value

    def __eq__(self, other):
        if isinstance(other, DataType):
            return self.value == other.value
        elif isinstance(other, (int, float, bool)):
            return self.value == other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ne__(self, other):
        if isinstance(other, DataType):
            return self.value != other.value
        elif self._is_compatible_with_datatype(other):
            return self.value != other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __gt__(self, other):
        if isinstance(other, DataType):
            return self.value > other.value
        elif self._is_compatible_with_datatype(other):
            return self.value > other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ge__(self, other):
        if isinstance(other, DataType):
            return self.value >= other.value
        elif self._is_compatible_with_datatype(other):
            return self.value >= other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __lt__(self, other):
        if isinstance(other, DataType):
            return self.value < other.value
        elif self._is_compatible_with_datatype(other):
            return self.value < other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __inv__(self):
        self.__invert__()

    def __invert__(self):
        if isinstance(self, (I32Value, I64Value, U32Value, U64Value)):
            return ~self.value
        elif isinstance(self, (BooleanValue, DoubleValue)):
            return 0
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __le__(self, other):
        if isinstance(other, DataType):
            return self.value <= other.value
        elif self._is_compatible_with_datatype(other):
            return self.value <= other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    @property
    def value(self):
        return self._data_value.Value

    @value.setter
    def value(self, newvalue):
        self._data_value.Value = self._to_data_value(newvalue).Value


class ArrayType(DataType):
    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(_errormessages.invalid_type_to_convert)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        return nivsexceptions.VeristandError(_errormessages.cannot_change_array_elements)


class ChannelReference(DataType):
    def __init__(self, value, description="", units=""):
        super(ChannelReference, self).__init__(value, description, units)
        self._channel_name = value

    @property
    def value(self):
        return realtimesequencedefinition.get_channel_value(self._channel_name)

    @value.setter
    def value(self, newvalue):
        realtimesequencedefinition.set_channel_value(self._channel_name, newvalue)

    def _to_data_value(self, value):
        return ClientApiDoubleValue(value)


class VectorChannelReference(ArrayType):
    @property
    def value(self):
        return [DoubleValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        return ClientApiDoubleValueArray(value)

    def __getitem__(self, key):
        raise nivsexceptions.VeristandNotImplementedError()


class BooleanValue(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = bool(value)
        elif type(value) is str and str(value).lower() == 'true':
            value = True
        elif type(value) is str and str(value).lower() == 'false':
            value = False
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiBooleanValue(value)


class BooleanValueArray(ArrayType):
    @property
    def value(self):
        return [BooleanValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [BooleanValue(item).value for item in value]
        return ClientApiBooleanValueArray(values)


class DoubleValue(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = float(value)
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiDoubleValue(value)


class DoubleValueArray(ArrayType):
    @property
    def value(self):
        return [DoubleValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [DoubleValue(item).value for item in value]
        return ClientApiDoubleValueArray(values)


class I32Value(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemInt32(value)
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiI32Value(value)


class I32ValueArray(ArrayType):
    @property
    def value(self):
        return [I32Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [I32Value(item).value for item in value]
        return ClientApiI32ValueArray(values)


class I64Value(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemInt64(value)
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiI64Value(value)


class I64ValueArray(ArrayType):
    @property
    def value(self):
        return [I64Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [I64Value(item).value for item in value]
        return ClientApiI64ValueArray(values)


class U32Value(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemUInt32(value)
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiU32Value(value)


class U32ValueArray(ArrayType):
    @property
    def value(self):
        return [U32Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [U32Value(item).value for item in value]
        return ClientApiU32ValueArray(values)


class U64Value(DataType):
    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemUInt64(value)
        else:
            raise TypeError('%s can not be created from value "%s"' % (self.__class__.__name__, str(value)))
        return ClientApiU64Value(value)


class U64ValueArray(ArrayType):
    @property
    def value(self):
        return [U64Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [U64Value(item).value for item in value]
        return ClientApiU64ValueArray(values)


VALID_TYPES = {
    ArrayType.__name__: ArrayType,
    BooleanValue.__name__: BooleanValue,
    BooleanValueArray.__name__: BooleanValueArray,
    ChannelReference.__name__: ChannelReference,
    DoubleValue.__name__: DoubleValue,
    DoubleValueArray.__name__: DoubleValueArray,
    I32Value.__name__: I32Value,
    I32ValueArray.__name__: I32ValueArray,
    I64Value.__name__: I64Value,
    I64ValueArray.__name__: I64ValueArray,
    U32Value.__name__: U32Value,
    U32ValueArray.__name__: U32ValueArray,
    U64Value.__name__: U64Value,
    U64ValueArray.__name__: U64ValueArray,
    VectorChannelReference.__name__: VectorChannelReference,
}

VALID_RETURN_TYPES = {
    BooleanValue.__name__: BooleanValue,
    DoubleValue.__name__: DoubleValue,
    I32Value.__name__: I32Value,
    I64Value.__name__: I64Value,
    U32Value.__name__: U32Value,
    U64Value.__name__: U64Value
}

CHANNEL_REF_TYPES = {
    ChannelReference.__name__: ChannelReference,
    VectorChannelReference.__name__: VectorChannelReference
}
