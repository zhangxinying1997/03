from functools import wraps
import sys, traceback
import time
from  contextlib import contextmanager

def handle_error(re_raise=True,log_traceback=True,exc_type=(Exception),tries:int=1,delay:float=0.0,backoff=1):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            loop_number = tries
            try:
                return func(*args, **kwargs)
            except:
                exc_tuple = sys.exc_info()
            if re_raise or (exc_tuple[0] not in [exc_type]):
                while loop_number>0:
                    try:
                        return func(*args, **kwargs)
                    except exc_type:
                            if log_traceback:
                                exc_trace = sys.exc_info()[2]
                                formatted_traceback = ''.join(traceback.format_tb(exc_trace))
                                print(formatted_traceback)
                    loop_number= loop_number-1
                    time.sleep(delay*backoff)
        return wrapper
    return decorate


@contextmanager
def handle_error_context(re_raise=True,log_traceback=True,exc_type=(Exception)):
    @handle_error(re_raise,log_traceback,exc_type)
    def some_function(exc):
        raise exc
    try:
        yield
    except Exception as exc:
        some_function(exc)




if __name__ == '__main__':
    with handle_error_context ( log_traceback =True , exc_type = ValueError ):
        raise ValueError