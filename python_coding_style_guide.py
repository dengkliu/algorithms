# Iterator 

Yes:  
      # Dictionary
      for key in adict: ...
      if key not in adict: ...
      # List
      if obj in alist: ...
      # Array
      if obj in anarray: ...
      for line in afile: ...
      # Dictionary 
      for k, v in adict.items(): ...
      for k, v in six.iteritems(adict): ...


# Default Argument Values
    def foo(a, b=None):
         if b is None:
             b = []
    def foo(a, b: Optional[Sequence] = None):
         if b is None:
             b = []
    def foo(a, b: Sequence = ()):  # Empty tuple OK since tuples are immutable
         ...


# True/False Evaluations
# A quick “rule of thumb” is that all “empty” values are considered false, 
# so 0, None, [], {}, '' all evaluate as false in a boolean context.
# Always use if foo is None: (or is not None) to check for a None value. 
#	E.g., when testing whether a variable or argument that defaults to None was set to some other value. 
# 	The other value might be a value that’s false in a boolean context!
# Never compare a boolean variable to False using ==. Use if not x: instead. 
# If you need to distinguish False from None then chain the expressions, such as if not x and x is not None:.
# For sequences (strings, lists, tuples), use the fact that empty sequences are false, 
# so if seq: and if not seq: are preferable to if len(seq): and if not len(seq): respectively.
# When handling integers, implicit false may involve more risk than benefit 
# (i.e., accidentally handling None as 0). 
# You may compare a value which is known to be an integer (and is not the result of len()) against the integer 0.
Yes: if not users:
         print('no users')

     if i % 10 == 0:
         self.handle_multiple_of_ten()

     def f(x=None):
         if x is None:
             x = []

# Stack (first go last out)
    stack = []
    # 1. Add
    stack.append(a)
    # 2. Pop the tail
    stack.pop()
    # 3. Peek the tail
    stack[-1]

# Queue


