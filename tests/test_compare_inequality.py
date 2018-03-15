import sys

from niveristand import _decorators, RealTimeSequence, TranslateError, VeristandError
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@_decorators.nivs_rt_sequence
def return_constant():
    a = DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_bool_builtins():
    a = BooleanValue(True)
    a.value = True != True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@_decorators.nivs_rt_sequence
def notequal_bool_builtins1():
    a = BooleanValue(True)
    a.value = False != False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@_decorators.nivs_rt_sequence
def notequal_bool_builtins2():
    a = BooleanValue(False)
    a.value = False != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@_decorators.nivs_rt_sequence
def notequal_bool_builtins3():
    a = BooleanValue(False)
    a.value = True != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@_decorators.nivs_rt_sequence
def notequal_simple_numbers():
    a = BooleanValue(True)
    a.value = 1 != 1
    return a.value


@_decorators.nivs_rt_sequence
def notequal_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = 1 != DoubleValue(2)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) != DoubleValue(1)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(1) != I32Value(1)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(1) != DoubleValue(1)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(False)
    a.value = I32Value(1) != I32Value(2)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_multiple_types():
    a = BooleanValue(True)
    a.value = 1 != DoubleValue(1) != 1.0
    return a.value


@_decorators.nivs_rt_sequence
def notequal_multiple_types1():
    a = BooleanValue(False)
    a.value = 1 != I32Value(2) != 3.0 != DoubleValue(4)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq():
    a = BooleanValue(True)
    a.value = 5 != return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq1():
    a = BooleanValue(True)
    a.value = return_constant() != 5
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(5) != return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq3():
    a = BooleanValue(True)
    a.value = return_constant() != DoubleValue(5)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(5) != return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def notequal_use_rtseq5():
    a = BooleanValue(False)
    a.value = return_constant() != I32Value(1)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_with_parantheses():
    a = BooleanValue(False)
    a.value = 0 != (2 != 3)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_with_parantheses1():
    a = BooleanValue(False)
    a.value = 0 != (DoubleValue(2) != I32Value(5))
    return a.value


@_decorators.nivs_rt_sequence
def notequal_with_parantheses2():
    a = BooleanValue(False)
    a.value = DoubleValue(0) != (I32Value(2) != 3.0) != DoubleValue(4)
    return a.value


@_decorators.nivs_rt_sequence
def notequal_variables():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 1 != a
    return b.value


@_decorators.nivs_rt_sequence
def notequal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 1 != a.value
    return b.value


@_decorators.nivs_rt_sequence
def notequal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value != b.value
    return c.value


@_decorators.nivs_rt_sequence
def notequal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value != b.value
    return c.value


@_decorators.nivs_rt_sequence
def notequal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a != b
    return c.value


@_decorators.nivs_rt_sequence
def notequal_variable_rtseq():
    a = BooleanValue(False)
    b = DoubleValue(0)
    a.value = b.value != return_constant()
    return a.value


@_decorators.nivs_rt_sequence
def notequal_variable_rtseq1():
    a = BooleanValue(False)
    b = DoubleValue(0)
    a.value = return_constant() != b.value
    return a.value


@_decorators.nivs_rt_sequence
def notequal_to_channelref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 != b.value
    return a.value


@_decorators.nivs_rt_sequence
def notequal_binary_unary():
    a = BooleanValue(True)
    a.value = -1 != - 1
    return a.value


@_decorators.nivs_rt_sequence
def notequal_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 1 != 2 != 3 != 4
    return a.value


@_decorators.nivs_rt_sequence
def notequal_complex_expr():
    a = BooleanValue(False)
    a.value = 1 != (2 if 2 < 3 else 1)
    return a.value


# <editor-fold desc=Invalid tests>

@_decorators.nivs_rt_sequence
def notequal_invalid_variables():
    return a.value != b


@_decorators.nivs_rt_sequence
def notequal_invalid_variables1():
    return a.value != b.value


@_decorators.nivs_rt_sequence
def notequal_to_None():
    a = BooleanValue(0)
    a.value = None != 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@_decorators.nivs_rt_sequence
def notequal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = return_constant != 1
    return a.value

# </editor-fold>


run_tests = [
    (return_constant, (), 5),
    (notequal_bool_builtins, (), False),
    (notequal_bool_builtins1, (), False),
    (notequal_bool_builtins2, (), False),
    (notequal_bool_builtins3, (), True),
    (notequal_simple_numbers, (), False),
    (notequal_num_nivsdatatype, (), True),
    (notequal_nivsdatatype_nivsdatatype, (), False),
    (notequal_nivsdatatype_nivsdatatype1, (), False),
    (notequal_nivsdatatype_nivsdatatype2, (), False),
    (notequal_nivsdatatype_nivsdatatype3, (), True),
    (notequal_with_parantheses, (), True),
    (notequal_with_parantheses1, (), True),
    (notequal_with_parantheses2, (), True),
    (notequal_variables, (), False),
    (notequal_variables1, (), False),
    (notequal_variable_variable, (), True),
    (notequal_variable_variable1, (), False),
    (notequal_variable_variable2, (), False),
    (notequal_with_multiple_comparators, (), True),
    (notequal_binary_unary, (), False),
    (notequal_complex_expr, (), True),
    (notequal_use_rtseq, (), False),
    (notequal_use_rtseq1, (), False),
    (notequal_use_rtseq2, (), False),
    (notequal_use_rtseq3, (), False),
    (notequal_use_rtseq4, (), False),
    (notequal_use_rtseq5, (), True),
    (notequal_variable_rtseq, (), True),
    (notequal_variable_rtseq1, (), True),
    (notequal_to_channelref, (), True),
]

skip_tests = [
    (notequal_multiple_types, (), "SPE and Python treat 1 != 1.0 differently."),
    (notequal_multiple_types1, (), "SPE and Python treat 1 != 1.0 differently."),
]

fail_transform_tests = [
    (notequal_invalid_variables, (), TranslateError),
    (notequal_invalid_variables1, (), TranslateError),
    (notequal_to_None, (), TranslateError),
    (notequal_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
