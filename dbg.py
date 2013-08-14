import byteplay as bp 

def _insert_print(i, label, code_list):
	code_list.insert(i+1,(bp.PRINT_NEWLINE, None))
	code_list.insert(i+1,(bp.PRINT_ITEM, None))
	code_list.insert(i+1,(bp.BINARY_MODULO, None))
	code_list.insert(i+1,(bp.CALL_FUNCTION, 1))
	code_list.insert(i+1,(bp.LOAD_FAST, label))
	code_list.insert(i+1,(bp.LOAD_GLOBAL, 'str'))
	code_list.insert(i+1,(bp.LOAD_CONST, label+'=%s'))
	return i+8
	
def dbg(function):
	code = bp.Code.from_code(function.func_code)
	i = 0
	while i < len(code.code):
		bcode, label = code.code[i]
		if bcode == bp.STORE_FAST and isinstance(label, basestring):
			i = _insert_print(i, label, code.code)
			continue
		i+=1
	
	function.func_code = code.to_code()
	return function
	
	
	

	
	
	
	
	
