(*FIRST,) = [1, 2, 3]  # documenting code no fun
*FIRST, a, b = [1, 2, 3]  # documenting code no fun
a, b = [1, 2]  # documenting code no fun
c = 1

def not_covered():
	"""
 	empty
 	"""
	raise NotImplementedError()

def bar():
	"""
 	empty
        """
	pass


def bar2():
	"""
 	empty
        """
	raise NotImplementedError()

def bar3():
	"""
 	empty
        """
	pass
