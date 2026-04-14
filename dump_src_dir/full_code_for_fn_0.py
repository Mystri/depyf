
# Note: the following variables are used inside the guard function.
___check_tensors = '''None'''
___check_tensors_verbose = '''None'''
___check_global_state = '''<built-in method check of torch._C._dynamo.guards.GlobalStateGuard object at 0x7f528351ee70>'''
___check_torch_function_mode_stack = '''<function make_torch_function_mode_stack_guard.<locals>.check_torch_function_mode_stack at 0x7f5280df7420>'''
IsNonOverlappingAndDenseIndicator = '''<function eval_is_non_overlapping_and_dense at 0x7f5294e09260>'''
cast_symbool_to_symint_guardless = '''<function cast_symbool_to_symint_guardless at 0x7f5294e09440>'''
math = '''<module 'math' from '/root/miniconda3/lib/python3.12/lib-dynload/math.cpython-312-x86_64-linux-gnu.so'>'''
torch = '''<module 'torch' from '/root/miniconda3/lib/python3.12/site-packages/torch/__init__.py'>'''
___check_type_id = '''<built-in function check_type_id>'''
___check_obj_id = '''<built-in function check_obj_id>'''
___odict_getitem = '''<method '__getitem__' of 'dict' objects>'''
___key_to_id = '''<function key_to_id at 0x7f528cbea660>'''
___dict_version = '''<built-in function dict_version>'''
___dict_contains = '''<function _get_closure_vars.<locals>.<lambda> at 0x7f5280df7380>'''
___tuple_iterator_len = '''<method '__length_hint__' of 'tuple_iterator' objects>'''
___normalize_range_iter = '''<function normalize_range_iter at 0x7f528cbea160>'''
___tuple_iterator_getitem = '''<function tuple_iterator_getitem at 0x7f528cbea020>'''
___dataclass_fields = '''<function dataclass_fields at 0x7f528cbea0c0>'''
___get_torch_function_mode_stack_at = '''<function get_torch_function_mode_stack_at at 0x7f528cbee200>'''
__math_isnan = '''<built-in function isnan>'''
__numpy_isnan = '''<ufunc 'isnan'>'''
inf = '''inf'''
__load_module = '''<function import_module at 0x7f53dcf8b060>'''
utils_device = '''<module 'torch.utils._device' from '/root/miniconda3/lib/python3.12/site-packages/torch/utils/_device.py'>'''
device = '''<class 'torch.device'>'''
___from_numpy = '''<function from_numpy at 0x7f528ca5fe20>'''
___as_tensor = '''<function _as_tensor_fullprec at 0x7f52962eb420>'''
inspect = '''<module 'inspect' from '/root/miniconda3/lib/python3.12/inspect.py'>'''
def __guard_0_for_fn(L, G, **___kwargs_ignored):
    __guard_hit = True
    __guard_hit = __guard_hit and torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:633 in init_ambient_guards
    __guard_hit = __guard_hit and utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:621 in init_ambient_guards
    __guard_hit = __guard_hit and ___check_global_state()
    __guard_hit = __guard_hit and ___check_torch_function_mode_stack()
    __guard_hit = __guard_hit and check_tensor(L['x'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 2], stride=[2, 1])
    __guard_hit = __guard_hit and hasattr(L['x'], '_dynamo_dynamic_indices') == False
    __guard_hit = __guard_hit and check_no_aliasing(L['x'], L['y'])
    __guard_hit = __guard_hit and check_tensor(L['y'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 2], stride=[2, 1])
    __guard_hit = __guard_hit and hasattr(L['y'], '_dynamo_dynamic_indices') == False
    return __guard_hit

# Note: please refer to the graph code in __compiled_fn_1_7144e863_95fe_4421_964d_ca34cb782af8*.py.
# Captured Graph: Dynamo generated graph (debuggable when using eager backend).
# Joint graph: joint forward+backward graph from aot autograd.
# Forward graph: forward graph from aot autograd (debuggable when using aot_eager backend).
# Backward graph: backward graph from aot autograd (debuggable when using aot_eager backend).
# AFTER XXX: graph processed by inductor (not debuggable).
def __compiled_fn_1_7144e863_95fe_4421_964d_ca34cb782af8(*args, **kwargs):
    pass

def __transformed_code_0_for_fn(x, y):
    tmp_1 = __import_torch_dot__dynamo_dot_utils.record_pregraph_bytecode_enter
    tmp_2 = __import_torch_dot__dynamo_dot_utils.record_pregraph_bytecode_enter()
    tmp_3 = __import_torch_dot__dynamo_dot_utils.record_pregraph_bytecode_exit
    __import_torch_dot__dynamo_dot_utils.record_pregraph_bytecode_exit(tmp_2)
    graph_out_0 = __compiled_fn_1_7144e863_95fe_4421_964d_ca34cb782af8(x, y)
    return graph_out_0[0]


# Note: if there is a transformed version below, this function might well not be executed directly. Please check the transformed version if possible.
def fn(x, y):
    return x.sin().cos() + y

def transformed_fn(x, y):
    __local_dict = {"x": x, "y": y}
    __global_dict = globals()
    if __guard_0_for_fn(__local_dict, __global_dict):
        return __transformed_code_0_for_fn(x, y)
    # Note: this function might well not be executed directly. It might well be transformed again, i.e. adding one more guards and transformed code.
    return fn(x, y)

#============ end of fn ============#
