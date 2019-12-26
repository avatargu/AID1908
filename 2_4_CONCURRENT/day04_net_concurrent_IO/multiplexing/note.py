import select

print("========== dir ==========:")
for item in dir(select)[-4:]:
    print(item)
"""
epoll
error
poll
select
"""

print("========== help ==========:")
# help(select.select)
"""
Help on built-in function select in module select:

select(...)
    select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
    
    Wait until one or more file descriptors are ready for some kind of I/O.
    The first three arguments are sequences of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    If only one kind of condition is required, pass [] for the other lists.
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows, only sockets are supported; on Unix, all file
    descriptors can be used.
"""

# help(select.poll)
"""
Help on built-in function poll in module select:

poll(...)
    Returns a polling object, which supports registering and
    unregistering file descriptors, and then polling them for I/O events.
"""

help(select.epoll)
"""
Help on class epoll in module select:

class epoll(builtins.object)
 |  select.epoll(sizehint=-1, flags=0)
 |  
 |  Returns an epolling object
 |  
 |  sizehint must be a positive integer or -1 for the default size. The
 |  sizehint is used to optimize internal data structures. It doesn't limit
 |  the maximum number of monitored events.
 |  
 |  Methods defined here:
 |  
 |  __enter__(...)
 |  
 |  __exit__(...)
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  close(...)
 |      close() -> None
 |      
 |      Close the epoll control file descriptor. Further operations on the epoll
 |      object will raise an exception.
 |  
 |  fileno(...)
 |      fileno() -> int
 |      
 |      Return the epoll control file descriptor.
 |  
 |  fromfd(...) from builtins.type
 |      fromfd(fd) -> epoll
 |      
 |      Create an epoll object from a given control fd.
 |  
 |  modify(...)
 |      modify(fd, eventmask) -> None
 |      
 |      fd is the target file descriptor of the operation
 |      events is a bit set composed of the various EPOLL constants
 |  
 |  poll(...)
 |      poll([timeout=-1[, maxevents=-1]]) -> [(fd, events), (...)]
 |      
 |      Wait for events on the epoll file descriptor for a maximum time of timeout
 |      in seconds (as float). -1 makes poll wait indefinitely.
 |      Up to maxevents are returned to the caller.
 |  
 |  register(...)
 |      register(fd[, eventmask]) -> None
 |      
 |      Registers a new fd or raises an OSError if the fd is already registered.
 |      fd is the target file descriptor of the operation.
 |      events is a bit set composed of the various EPOLL constants; the default
 |      is EPOLLIN | EPOLLOUT | EPOLLPRI.
 |      
 |      The epoll interface supports all file descriptors that support poll.
 |  
 |  unregister(...)
 |      unregister(fd) -> None
 |      
 |      fd is the target file descriptor of the operation.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  closed
 |      True if the epoll handler is closed
"""
