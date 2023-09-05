import inspect

def retrieve_var_name() -> str:
    """Retrieve variable name from the caller's scope which code not start with
    space."""
    frames = inspect.getouterframes(inspect.currentframe())

    for f in frames[1:]:  # Skip the current frame
        code_ctx = f.code_context
        if code_ctx is not None and not code_ctx[0].startswith(" "):
            return code_ctx[0].split("=")[0].strip()
    msg = "Cannot find variable name"
    raise ValueError(msg)