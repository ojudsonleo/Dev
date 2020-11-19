import os
from _socket import SocketType
from socket import SocketKind, AddressFamily
from typing import Union


class judson(object):
    import abc
    import array
    import bdb as db
    import builtins as builtin
    import builtins as Builtins
    import calendar
    import collections
    import csv
    import datetime
    import email
    import enum as Enum
    import importlib
    import itertools
    import json
    import math
    import os as system
    import pwd
    import random
    import runpy as RunPy
    import sys as jsys
    import time
    import turtle as turtle
    import webbrowser as WebBrowser
    import mailbox as MailBox
    import easy_install as install
    import socket

    i = itertools
    i1 = importlib
    i2 = collections
    i3 = csv
    i4 = math
    i5 = json
    i6 = datetime
    i7 = turtle
    i8 = random
    i9 = system
    i10 = jsys
    i11 = email
    i12 = calendar
    i13 = time
    i14 = array
    i15 = abc
    i16 = install
    i17 = Enum
    i18 = builtin
    i19 = pwd
    i20 = Enum
    i21 = db
    i22 = Builtins
    i23 = RunPy
    i24 = WebBrowser
    i25 = MailBox

    @staticmethod
    def Socket():
        # Wrapper module for _socket, providing some additional facilities
        # implemented in Python.

        """\
        This module provides socket operations and some related functions.
        On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
        On other systems, it only supports IP. Functions specific for a
        socket are available as methods of the socket object.

        Functions:

        socket() -- create a new socket object
        socketpair() -- create a pair of new socket objects [*]
        fromfd() -- create a socket object from an open file descriptor [*]
        send_fds() -- Send file descriptor to the socket.
        recv_fds() -- Recieve file descriptors from the socket.
        fromshare() -- create a socket object from data received from socket.share() [*]
        gethostname() -- return the current hostname
        gethostbyname() -- map a hostname to its IP number
        gethostbyaddr() -- map an IP number or hostname to DNS info
        getservbyname() -- map a service name and a protocol name to a port number
        getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
        ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
        htons(), htonl() -- convert 16, 32 bit int from host to network byte order
        inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
        inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
        socket.getdefaulttimeout() -- get the default timeout value
        socket.setdefaulttimeout() -- set the default timeout value
        create_connection() -- connects to an address, with an optional timeout and
                               optional source address.

         [*] not available on all platforms!

        Special objects:

        SocketType -- type object for socket objects
        error -- exception raised for I/O errors
        has_ipv6 -- boolean value indicating if IPv6 is supported

        IntEnum constants:

        AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
        SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

        Integer constants:

        Many other constants may be defined; these may be used in calls to
        the setsockopt() and getsockopt() methods.
        """

        import _socket
        from _socket import *

        import os, sys, io, selectors
        from enum import IntEnum, IntFlag

        try:
            import errno
        except ImportError:
            errno = None
        EBADF = getattr(errno, 'EBADF', 9)
        EAGAIN = getattr(errno, 'EAGAIN', 11)
        EWOULDBLOCK = getattr(errno, 'EWOULDBLOCK', 11)

        __all__ = ["fromfd", "getfqdn", "create_connection", "create_server",
                   "has_dualstack_ipv6", "AddressFamily", "SocketKind"]
        __all__.extend(os._get_exports_list(_socket))

        # Set up the socket.AF_* socket.SOCK_* constants as members of IntEnums for
        # nicer string representations.
        # Note that _socket only knows about the integer values. The public interface
        # in this module understands the enums and translates them back from integers
        # where needed (e.g. .family property of a socket object).

        IntEnum._convert_(
            'AddressFamily',
            __name__,
            lambda C: C.isupper() and C.startswith('AF_'))

        IntEnum._convert_(
            'SocketKind',
            __name__,
            lambda C: C.isupper() and C.startswith('SOCK_'))

        IntFlag._convert_(
            'MsgFlag',
            __name__,
            lambda C: C.isupper() and C.startswith('MSG_'))

        IntFlag._convert_(
            'AddressInfo',
            __name__,
            lambda C: C.isupper() and C.startswith('AI_'))

        _LOCALHOST = '127.0.0.1'
        _LOCALHOST_V6 = '::1'

        def _intenum_converter(value, enum_klass):
            """Convert a numeric family value to an IntEnum member.

            If it's not a known member, return the numeric value itself.
            """
            try:
                return enum_klass(value)
            except ValueError:
                return value

        # WSA error codes
        if sys.platform.lower().startswith("win"):
            errorTab = {}
            errorTab[6] = "Specified event object handle is invalid."
            errorTab[8] = "Insufficient memory available."
            errorTab[87] = "One or more parameters are invalid."
            errorTab[995] = "Overlapped operation aborted."
            errorTab[996] = "Overlapped I/O event object not in signaled state."
            errorTab[997] = "Overlapped operation will complete later."
            errorTab[10004] = "The operation was interrupted."
            errorTab[10009] = "A bad file handle was passed."
            errorTab[10013] = "Permission denied."
            errorTab[10014] = "A fault occurred on the network??"  # WSAEFAULT
            errorTab[10022] = "An invalid operation was attempted."
            errorTab[10024] = "Too many open files."
            errorTab[10035] = "The socket operation would block"
            errorTab[10036] = "A blocking operation is already in progress."
            errorTab[10037] = "Operation already in progress."
            errorTab[10038] = "Socket operation on nonsocket."
            errorTab[10039] = "Destination address required."
            errorTab[10040] = "Message too long."
            errorTab[10041] = "Protocol wrong type for socket."
            errorTab[10042] = "Bad protocol option."
            errorTab[10043] = "Protocol not supported."
            errorTab[10044] = "Socket type not supported."
            errorTab[10045] = "Operation not supported."
            errorTab[10046] = "Protocol family not supported."
            errorTab[10047] = "Address family not supported by protocol family."
            errorTab[10048] = "The network address is in use."
            errorTab[10049] = "Cannot assign requested address."
            errorTab[10050] = "Network is down."
            errorTab[10051] = "Network is unreachable."
            errorTab[10052] = "Network dropped connection on reset."
            errorTab[10053] = "Software caused connection abort."
            errorTab[10054] = "The connection has been reset."
            errorTab[10055] = "No buffer space available."
            errorTab[10056] = "Socket is already connected."
            errorTab[10057] = "Socket is not connected."
            errorTab[10058] = "The network has been shut down."
            errorTab[10059] = "Too many references."
            errorTab[10060] = "The operation timed out."
            errorTab[10061] = "Connection refused."
            errorTab[10062] = "Cannot translate name."
            errorTab[10063] = "The name is too long."
            errorTab[10064] = "The host is down."
            errorTab[10065] = "The host is unreachable."
            errorTab[10066] = "Directory not empty."
            errorTab[10067] = "Too many processes."
            errorTab[10068] = "User quota exceeded."
            errorTab[10069] = "Disk quota exceeded."
            errorTab[10070] = "Stale file handle reference."
            errorTab[10071] = "Item is remote."
            errorTab[10091] = "Network subsystem is unavailable."
            errorTab[10092] = "Winsock.dll version out of range."
            errorTab[10093] = "Successful WSAStartup not yet performed."
            errorTab[10101] = "Graceful shutdown in progress."
            errorTab[10102] = "No more results from WSALookupServiceNext."
            errorTab[10103] = "Call has been canceled."
            errorTab[10104] = "Procedure call table is invalid."
            errorTab[10105] = "Service provider is invalid."
            errorTab[10106] = "Service provider failed to initialize."
            errorTab[10107] = "System call failure."
            errorTab[10108] = "Service not found."
            errorTab[10109] = "Class type not found."
            errorTab[10110] = "No more results from WSALookupServiceNext."
            errorTab[10111] = "Call was canceled."
            errorTab[10112] = "Database query was refused."
            errorTab[11001] = "Host not found."
            errorTab[11002] = "Nonauthoritative host not found."
            errorTab[11003] = "This is a nonrecoverable error."
            errorTab[11004] = "Valid name, no data record requested type."
            errorTab[11005] = "QoS receivers."
            errorTab[11006] = "QoS senders."
            errorTab[11007] = "No QoS senders."
            errorTab[11008] = "QoS no receivers."
            errorTab[11009] = "QoS request confirmed."
            errorTab[11010] = "QoS admission error."
            errorTab[11011] = "QoS policy failure."
            errorTab[11012] = "QoS bad style."
            errorTab[11013] = "QoS bad object."
            errorTab[11014] = "QoS traffic control error."
            errorTab[11015] = "QoS generic error."
            errorTab[11016] = "QoS service type error."
            errorTab[11017] = "QoS flowspec error."
            errorTab[11018] = "Invalid QoS provider buffer."
            errorTab[11019] = "Invalid QoS filter style."
            errorTab[11020] = "Invalid QoS filter style."
            errorTab[11021] = "Incorrect QoS filter count."
            errorTab[11022] = "Invalid QoS object length."
            errorTab[11023] = "Incorrect QoS flow count."
            errorTab[11024] = "Unrecognized QoS object."
            errorTab[11025] = "Invalid QoS policy object."
            errorTab[11026] = "Invalid QoS flow descriptor."
            errorTab[11027] = "Invalid QoS provider-specific flowspec."
            errorTab[11028] = "Invalid QoS provider-specific filterspec."
            errorTab[11029] = "Invalid QoS shape discard mode object."
            errorTab[11030] = "Invalid QoS shaping rate object."
            errorTab[11031] = "Reserved policy QoS element type."
            __all__.append("errorTab")

        class _GiveupOnSendfile(Exception):
            pass

        class socket(_socket.socket):

            """A subclass of _socket.socket adding the makefile() method."""

            __slots__ = ["__weakref__", "_io_refs", "_closed"]

            def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
                # For user code address family and type values are IntEnum members, but
                # for the underlying _socket.socket they're just integers. The
                # constructor of _socket.socket converts the given argument to an
                # integer automatically.
                if fileno is None:
                    if family == -1:
                        family = AF_INET
                    if type == -1:
                        type = SOCK_STREAM
                    if proto == -1:
                        proto = 0
                _socket.socket.__init__(self, family, type, proto, fileno)
                self._io_refs = 0
                self._closed = False

            def __enter__(self):
                return self

            def __exit__(self, *args):
                if not self._closed:
                    self.close()

            def __repr__(self):
                """Wrap __repr__() to reveal the real class name and socket
                address(es).
                """
                closed = getattr(self, '_closed', False)
                s = "<%s.%s%s fd=%i, family=%s, type=%s, proto=%i" \
                    % (self.__class__.__module__,
                       self.__class__.__qualname__,
                       " [closed]" if closed else "",
                       self.fileno(),
                       self.family,
                       self.type,
                       self.proto)
                if not closed:
                    try:
                        laddr = self.getsockname()
                        if laddr:
                            s += ", laddr=%s" % str(laddr)
                    except error:
                        pass
                    try:
                        raddr = self.getpeername()
                        if raddr:
                            s += ", raddr=%s" % str(raddr)
                    except error:
                        pass
                s += '>'
                return s

            def __getstate__(self):
                raise TypeError(f"cannot pickle {self.__class__.__name__!r} object")

            def dup(self):
                """dup() -> socket object

                Duplicate the socket. Return a new socket object connected to the same
                system resource. The new socket is non-inheritable.
                """
                fd = dup(self.fileno())
                sock = self.__class__(self.family, self.type, self.proto, fileno=fd)
                sock.settimeout(self.gettimeout())
                return sock

            def accept(self):
                """accept() -> (socket object, address info)

                Wait for an incoming connection.  Return a new socket
                representing the connection, and the address of the client.
                For IP sockets, the address info is a pair (hostaddr, port).
                """
                fd, addr = self._accept()
                sock = socket(self.family, self.type, self.proto, fileno=fd)
                # Issue #7995: if no default timeout is set and the listening
                # socket had a (non-zero) timeout, force the new socket in blocking
                # mode to override platform-specific socket flags inheritance.
                if getdefaulttimeout() is None and self.gettimeout():
                    sock.setblocking(True)
                return sock, addr

            def makefile(self, mode="r", buffering=None, *,
                         encoding=None, errors=None, newline=None):
                """makefile(...) -> an I/O stream connected to the socket

                The arguments are as for io.open() after the filename, except the only
                supported mode values are 'r' (default), 'w' and 'b'.
                """
                # XXX refactor to share code?
                if not set(mode) <= {"r", "w", "b"}:
                    raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))
                writing = "w" in mode
                reading = "r" in mode or not writing
                assert reading or writing
                binary = "b" in mode
                rawmode = ""
                if reading:
                    rawmode += "r"
                if writing:
                    rawmode += "w"
                raw = SocketIO(self, rawmode)
                self._io_refs += 1
                if buffering is None:
                    buffering = -1
                if buffering < 0:
                    buffering = io.DEFAULT_BUFFER_SIZE
                if buffering == 0:
                    if not binary:
                        raise ValueError("unbuffered streams must be binary")
                    return raw
                if reading and writing:
                    buffer = io.BufferedRWPair(raw, raw, buffering)
                elif reading:
                    buffer = io.BufferedReader(raw, buffering)
                else:
                    assert writing
                    buffer = io.BufferedWriter(raw, buffering)
                if binary:
                    return buffer
                text = io.TextIOWrapper(buffer, encoding, errors, newline)
                text.mode = mode
                return text

            if hasattr(os, 'sendfile'):

                def _sendfile_use_sendfile(self, file, offset=0, count=None):
                    self._check_sendfile_params(file, offset, count)
                    sockno = self.fileno()
                    try:
                        fileno = file.fileno()
                    except (AttributeError, io.UnsupportedOperation) as err:
                        raise _GiveupOnSendfile(err)  # not a regular file
                    try:
                        fsize = os.fstat(fileno).st_size
                    except OSError as err:
                        raise _GiveupOnSendfile(err)  # not a regular file
                    if not fsize:
                        return 0  # empty file
                    # Truncate to 1GiB to avoid OverflowError, see bpo-38319.
                    blocksize = min(count or fsize, 2 ** 30)
                    timeout = self.gettimeout()
                    if timeout == 0:
                        raise ValueError("non-blocking sockets are not supported")
                    # poll/select have the advantage of not requiring any
                    # extra file descriptor, contrarily to epoll/kqueue
                    # (also, they require a single syscall).
                    if hasattr(selectors, 'PollSelector'):
                        selector = selectors.PollSelector()
                    else:
                        selector = selectors.SelectSelector()
                    selector.register(sockno, selectors.EVENT_WRITE)

                    total_sent = 0
                    # localize variable access to minimize overhead
                    selector_select = selector.select
                    os_sendfile = os.sendfile
                    try:
                        while True:
                            if timeout and not selector_select(timeout):
                                raise _socket.timeout('timed out')
                            if count:
                                blocksize = count - total_sent
                                if blocksize <= 0:
                                    break
                            try:
                                sent = os_sendfile(sockno, fileno, offset, blocksize)
                            except BlockingIOError:
                                if not timeout:
                                    # Block until the socket is ready to send some
                                    # data; avoids hogging CPU resources.
                                    selector_select()
                                continue
                            except OSError as err:
                                if total_sent == 0:
                                    # We can get here for different reasons, the main
                                    # one being 'file' is not a regular mmap(2)-like
                                    # file, in which case we'll fall back on using
                                    # plain send().
                                    raise _GiveupOnSendfile(err)
                                raise err from None
                            else:
                                if sent == 0:
                                    break  # EOF
                                offset += sent
                                total_sent += sent
                        return total_sent
                    finally:
                        if total_sent > 0 and hasattr(file, 'seek'):
                            file.seek(offset)
            else:
                def _sendfile_use_sendfile(self, file, offset=0, count=None):
                    raise _GiveupOnSendfile(
                        "os.sendfile() not available on this platform")

            def _sendfile_use_send(self, file, offset=0, count=None):
                self._check_sendfile_params(file, offset, count)
                if self.gettimeout() == 0:
                    raise ValueError("non-blocking sockets are not supported")
                if offset:
                    file.seek(offset)
                blocksize = min(count, 8192) if count else 8192
                total_sent = 0
                # localize variable access to minimize overhead
                file_read = file.read
                sock_send = self.send
                try:
                    while True:
                        if count:
                            blocksize = min(count - total_sent, blocksize)
                            if blocksize <= 0:
                                break
                        data = memoryview(file_read(blocksize))
                        if not data:
                            break  # EOF
                        while True:
                            try:
                                sent = sock_send(data)
                            except BlockingIOError:
                                continue
                            else:
                                total_sent += sent
                                if sent < len(data):
                                    data = data[sent:]
                                else:
                                    break
                    return total_sent
                finally:
                    if total_sent > 0 and hasattr(file, 'seek'):
                        file.seek(offset + total_sent)

            def _check_sendfile_params(self, file, offset, count):
                if 'b' not in getattr(file, 'mode', 'b'):
                    raise ValueError("file should be opened in binary mode")
                if not self.type & SOCK_STREAM:
                    raise ValueError("only SOCK_STREAM type sockets are supported")
                if count is not None:
                    if not isinstance(count, int):
                        raise TypeError(
                            "count must be a positive integer (got {!r})".format(count))
                    if count <= 0:
                        raise ValueError(
                            "count must be a positive integer (got {!r})".format(count))

            def sendfile(self, file, offset=0, count=None):
                """sendfile(file[, offset[, count]]) -> sent

                Send a file until EOF is reached by using high-performance
                os.sendfile() and return the total number of bytes which
                were sent.
                *file* must be a regular file object opened in binary mode.
                If os.sendfile() is not available (e.g. Windows) or file is
                not a regular file socket.send() will be used instead.
                *offset* tells from where to start reading the file.
                If specified, *count* is the total number of bytes to transmit
                as opposed to sending the file until EOF is reached.
                File position is updated on return or also in case of error in
                which case file.tell() can be used to figure out the number of
                bytes which were sent.
                The socket must be of SOCK_STREAM type.
                Non-blocking sockets are not supported.
                """
                try:
                    return self._sendfile_use_sendfile(file, offset, count)
                except _GiveupOnSendfile:
                    return self._sendfile_use_send(file, offset, count)

            def _decref_socketios(self):
                if self._io_refs > 0:
                    self._io_refs -= 1
                if self._closed:
                    self.close()

            def _real_close(self, _ss=_socket.socket):
                # This function should not reference any globals. See issue #808164.
                _ss.close(self)

            def close(self):
                # This function should not reference any globals. See issue #808164.
                self._closed = True
                if self._io_refs <= 0:
                    self._real_close()

            def detach(self):
                """detach() -> file descriptor

                Close the socket object without closing the underlying file descriptor.
                The object cannot be used after this call, but the file descriptor
                can be reused for other purposes.  The file descriptor is returned.
                """
                self._closed = True
                return super().detach()

            @property
            def family(self):
                """Read-only access to the address family for this socket.
                """
                return _intenum_converter(super().family, AddressFamily)

            @property
            def type(self):
                """Read-only access to the socket type.
                """
                return _intenum_converter(super().type, SocketKind)

            if os.name == 'nt':
                def get_inheritable(self):
                    return os.get_handle_inheritable(self.fileno())

                def set_inheritable(self, inheritable):
                    os.set_handle_inheritable(self.fileno(), inheritable)
            else:
                def get_inheritable(self):
                    return os.get_inheritable(self.fileno())

                def set_inheritable(self, inheritable):
                    os.set_inheritable(self.fileno(), inheritable)
            get_inheritable.__doc__ = "Get the inheritable flag of the socket"
            set_inheritable.__doc__ = "Set the inheritable flag of the socket"

        def fromfd(fd, family, type, proto=0):
            """ fromfd(fd, family, type[, proto]) -> socket object

            Create a socket object from a duplicate of the given file
            descriptor.  The remaining arguments are the same as for socket().
            """
            nfd = dup(fd)
            return socket(family, type, proto, nfd)

        if hasattr(_socket.socket, "sendmsg"):
            import array

            def send_fds(sock, buffers, fds, flags=0, address=None):
                """ send_fds(sock, buffers, fds[, flags[, address]]) -> integer

                Send the list of file descriptors fds over an AF_UNIX socket.
                """
                return sock.sendmsg(buffers, [(_socket.SOL_SOCKET,
                                               _socket.SCM_RIGHTS, array.array("i", fds))])

            __all__.append("send_fds")

        if hasattr(_socket.socket, "recvmsg"):
            import array

            def recv_fds(sock, bufsize, maxfds, flags=0):
                """ recv_fds(sock, bufsize, maxfds[, flags]) -> (data, list of file
                descriptors, msg_flags, address)

                Receive up to maxfds file descriptors returning the message
                data and a list containing the descriptors.
                """
                # Array of ints
                fds = array.array("i")
                msg, ancdata, flags, addr = sock.recvmsg(bufsize,
                                                         _socket.CMSG_LEN(maxfds * fds.itemsize))
                for cmsg_level, cmsg_type, cmsg_data in ancdata:
                    if (cmsg_level == _socket.SOL_SOCKET and cmsg_type == _socket.SCM_RIGHTS):
                        fds.frombytes(cmsg_data[:
                                                len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])

                return msg, list(fds), flags, addr

            __all__.append("recv_fds")

        if hasattr(_socket.socket, "share"):
            def fromshare(info):
                """ fromshare(info) -> socket object

                Create a socket object from the bytes object returned by
                socket.share(pid).
                """
                return socket(0, 0, 0, info)

            __all__.append("fromshare")

        if hasattr(_socket, "socketpair"):

            def socketpair(family=None, type=SOCK_STREAM, proto=0):
                """socketpair([family[, type[, proto]]]) -> (socket object, socket object)

                Create a pair of socket objects from the sockets returned by the platform
                socketpair() function.
                The arguments are the same as for socket() except the default family is
                AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
                """
                if family is None:
                    try:
                        family = AF_UNIX
                    except NameError:
                        family = AF_INET
                a, b = _socket.socketpair(family, type, proto)
                a = socket(family, type, proto, a.detach())
                b = socket(family, type, proto, b.detach())
                return a, b

        else:

            # Origin: https://gist.github.com/4325783, by Geert Jansen.  Public domain.
            def socketpair(family=AF_INET, type=SOCK_STREAM, proto=0):
                global AF_INET, SOCK_STREAM
                if family == AF_INET:
                    host = _LOCALHOST
                elif family == AF_INET6:
                    host = _LOCALHOST_V6
                else:
                    raise ValueError("Only AF_INET and AF_INET6 socket address families "
                                     "are supported")
                if type != SOCK_STREAM:
                    raise ValueError("Only SOCK_STREAM socket type is supported")
                if proto != 0:
                    raise ValueError("Only protocol zero is supported")

                # We create a connected TCP socket. Note the trick with
                # setblocking(False) that prevents us from having to create a thread.
                lsock = socket(family, type, proto)
                try:
                    lsock.bind((host, 0))
                    lsock.listen()
                    # On IPv6, ignore flow_info and scope_id
                    addr, port = lsock.getsockname()[:2]
                    csock = socket(family, type, proto)
                    try:
                        csock.setblocking(False)
                        try:
                            csock.connect((addr, port))
                        except (BlockingIOError, InterruptedError):
                            pass
                        csock.setblocking(True)
                        ssock: Union[socket, SocketType]
                        ssock, _ = lsock.accept()
                    except:
                        csock.close()
                        raise
                finally:
                    lsock.close()
                return csock, ssock

            __all__.append("socketpair")

        socketpair.__doc__ = """socketpair([family[, type[, proto]]]) -> (socket object, socket object)
        Create a pair of socket objects from the sockets returned by the platform
        The arguments are the same as for socket() except the default family is AF_UNIX
        if defined on the platform; otherwise, the default is AF_INET.
        """

        _blocking_errnos = {EAGAIN, EWOULDBLOCK}

        class SocketIO(io.RawIOBase):

            """Raw I/O implementation for stream sockets.

            This class supports the makefile() method on sockets.  It provides
            the raw I/O interface on top of a socket object.
            """

            # One might wonder why not let FileIO do the job instead.  There are two
            # main reasons why FileIO is not adapted:
            # - it wouldn't work under Windows (where you can't used read() and
            #   write() on a socket handle)
            # - it wouldn't work with socket timeouts (FileIO would ignore the
            #   timeout and consider the socket non-blocking)

            # XXX More docs

            def __init__(self, sock, mode):
                if mode not in ("r", "w", "rw", "rb", "wb", "rwb"):
                    raise ValueError("invalid mode: %r" % mode)
                io.RawIOBase.__init__(self)
                self._sock = sock
                if "b" not in mode:
                    mode += "b"
                self._mode = mode
                self._reading = "r" in mode
                self._writing = "w" in mode
                self._timeout_occurred = False

            def readinto(self, b):
                """Read up to len(b) bytes into the writable buffer *b* and return
                the number of bytes read.  If the socket is non-blocking and no bytes
                are available, None is returned.

                If *b* is non-empty, a 0 return value indicates that the connection
                was shutdown at the other end.
                """
                self._checkClosed()
                self._checkReadable()
                if self._timeout_occurred:
                    raise OSError("cannot read from timed out object")
                while True:
                    try:
                        return self._sock.recv_into(b)
                    except timeout:
                        self._timeout_occurred = True
                        raise
                    except error as e:
                        if e.args[0] in _blocking_errnos:
                            return None
                        raise

            def write(self, b):
                """Write the given bytes or bytearray object *b* to the socket
                and return the number of bytes written.  This can be less than
                len(b) if not all data could be written.  If the socket is
                non-blocking and no bytes could be written None is returned.
                """
                self._checkClosed()
                self._checkWritable()
                try:
                    return self._sock.send(b)
                except error as e:
                    # XXX what about EINTR?
                    if e.args[0] in _blocking_errnos:
                        return None
                    raise

            def readable(self):
                """True if the SocketIO is open for reading.
                """
                if self.closed:
                    raise ValueError("I/O operation on closed socket.")
                return self._reading

            def writable(self):
                """True if the SocketIO is open for writing.
                """
                if self.closed:
                    raise ValueError("I/O operation on closed socket.")
                return self._writing

            def seekable(self):
                """True if the SocketIO is open for seeking.
                """
                if self.closed:
                    raise ValueError("I/O operation on closed socket.")
                return super().seekable()

            def fileno(self):
                """Return the file descriptor of the underlying socket.
                """
                self._checkClosed()
                return self._sock.fileno()

            @property
            def name(self):
                if not self.closed:
                    return self.fileno()
                else:
                    return -1

            @property
            def mode(self):
                return self._mode

            def close(self):
                """Close the SocketIO object.  This doesn't close the underlying
                socket, except if all references to it have disappeared.
                """
                if self.closed:
                    return

                io.RawIOBase.close(self)
                self._sock = None

            def _checkWritable(self):
                pass

            def _checkReadable(self):
                pass

        _GLOBAL_DEFAULT_TIMEOUT = object()

        def has_dualstack_ipv6():
            """Return True if the platform supports creating a SOCK_STREAM socket
            which can handle both AF_INET and AF_INET6 (IPv4 / IPv6) connections.
            """
            if not has_ipv6 \
                    or not hasattr(_socket, 'IPPROTO_IPV6') \
                    or not hasattr(_socket, 'IPV6_V6ONLY'):
                return False
            try:
                with socket(AF_INET6, SOCK_STREAM) as sock:
                    sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
                    return True
            except error:
                return False

        def create_server(address, *, family=AF_INET, backlog=None, reuse_port=False,
                          dualstack_ipv6=False):
            """Convenience function which creates a SOCK_STREAM type socket
            bound to *address* (a 2-tuple (host, port)) and return the socket
            object.

            *family* should be either AF_INET or AF_INET6.
            *backlog* is the queue size passed to socket.listen().
            *reuse_port* dictates whether to use the SO_REUSEPORT socket option.
            *dualstack_ipv6*: if true and the platform supports it, it will
            create an AF_INET6 socket able to accept both IPv4 or IPv6
            connections. When false it will explicitly disable this option on
            platforms that enable it by default (e.g. Linux).

            >>> with create_server(('', 8000)) as server:
            ...     while True:
            ...         conn, addr = server.accept()
            ...         # handle new connection
            """
            if reuse_port and not hasattr(_socket, "SO_REUSEPORT"):
                raise ValueError("SO_REUSEPORT not supported on this platform")
            if dualstack_ipv6:
                if not has_dualstack_ipv6():
                    raise ValueError("dualstack_ipv6 not supported on this platform")
                if family != AF_INET6:
                    raise ValueError("dualstack_ipv6 requires AF_INET6 family")
            sock = socket(family, SOCK_STREAM)
            try:
                # Note about Windows. We don't set SO_REUSEADDR because:
                # 1) It's unnecessary: bind() will succeed even in case of a
                # previous closed socket on the same address and still in
                # TIME_WAIT state.
                # 2) If set, another socket is free to bind() on the same
                # address, effectively preventing this one from accepting
                # connections. Also, it may set the process in a state where
                # it'll no longer respond to any signals or graceful kills.
                # See: msdn2.microsoft.com/en-us/library/ms740621(VS.85).aspx
                if os.name not in ('nt', 'cygwin') and \
                        hasattr(_socket, 'SO_REUSEADDR'):
                    try:
                        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
                    except error:
                        # Fail later on bind(), for platforms which may not
                        # support this option.
                        pass
                if reuse_port:
                    sock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
                if has_ipv6 and family == AF_INET6:
                    if dualstack_ipv6:
                        sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
                    elif hasattr(_socket, "IPV6_V6ONLY") and \
                            hasattr(_socket, "IPPROTO_IPV6"):
                        sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 1)
                try:
                    sock.bind(address)
                except error as err:
                    msg = '%s (while attempting to bind on address %r)' % \
                          (err.strerror, address)
                    raise error(err.errno, msg) from None
                if backlog is None:
                    sock.listen()
                else:
                    sock.listen(backlog)
                return sock
            except error:
                sock.close()
                raise

    @staticmethod
    def GraphLib():

        _NODE_OUT = -1
        _NODE_DONE = -2

    @staticmethod
    def Chat():
        import webbrowser
        webbrowser.open(
            "http://localhost:63342/judson/com/lib/zoom.html?_ijt=skvhjrtferh5luu3t5apmr5du4")

    @staticmethod
    def Symtable():
        """Interface to the compiler's internal symbol tables"""

        import weakref

        import _symtable
        from _symtable import (CELL, DEF_ANNOT, DEF_IMPORT, DEF_LOCAL,
                               DEF_NONLOCAL, DEF_PARAM, FREE, GLOBAL_EXPLICIT,
                               GLOBAL_IMPLICIT, LOCAL, SCOPE_MASK, SCOPE_OFF)

        def symtable(code, filename, compile_type):
            top = _symtable.symtable(code, filename, compile_type)
            return _newSymbolTable(top, filename)

        class SymbolTableFactory:
            def __init__(self):
                self.__memo = weakref.WeakValueDictionary()

            @staticmethod
            def new(table, filename):
                if table.type == _symtable.TYPE_FUNCTION:
                    return Function(table, filename)
                if table.type == _symtable.TYPE_CLASS:
                    return Class(table, filename)
                return SymbolTable(table, filename)

            def __call__(self, table, filename):
                key = table, filename
                obj = self.__memo.get(key, None)
                if obj is None:
                    obj = self.__memo[key] = self.new(table, filename)
                return obj

        _newSymbolTable = SymbolTableFactory()

        class SymbolTable(object):

            def __init__(self, raw_table, filename):
                self._table = raw_table
                self._filename = filename
                self._symbols = {}

            def __repr__(self):
                if self.__class__ == SymbolTable:
                    kind = ""
                else:
                    kind = "%s " % self.__class__.__name__

                if self._table.name == "global":
                    return "<{0}SymbolTable for module {1}>".format(kind, self._filename)
                else:
                    return "<{0}SymbolTable for {1} in {2}>".format(kind,
                                                                    self._table.name,
                                                                    self._filename)

            def get_type(self):
                if self._table.type == _symtable.TYPE_MODULE:
                    return "module"
                if self._table.type == _symtable.TYPE_FUNCTION:
                    return "function"
                if self._table.type == _symtable.TYPE_CLASS:
                    return "class"
                assert self._table.type in (1, 2, 3), \
                    "unexpected type: {0}".format(self._table.type)

            def get_id(self):
                return self._table.id

            def get_name(self):
                return self._table.name

            def get_lineno(self):
                return self._table.lineno

            def is_optimized(self):
                return bool(self._table.type == _symtable.TYPE_FUNCTION)

            def is_nested(self):
                return bool(self._table.nested)

            def has_children(self):
                return bool(self._table.children)

            def get_identifiers(self):
                return self._table.symbols.keys()

            def lookup(self, name):
                sym = self._symbols.get(name)
                if sym is None:
                    flags = self._table.symbols[name]
                    sym = self._symbols[name] = Symbol(name, flags)
                return sym

            def get_symbols(self):
                return [self.lookup(Ident) for Ident in self.get_identifiers()]

            def get_children(self):
                return [_newSymbolTable(st, self._filename)
                        for st in self._table.children]

        class Function(SymbolTable):

            # Default values for instance variables
            __params = None
            __locals = None
            __frees = None
            __globals = None
            __nonlocals = None

            def __idents_matching(self, test_func):
                return tuple(Ident for Ident in self.get_identifiers()
                             if test_func(self._table.symbols[Ident]))

            def get_parameters(self):
                if self.__params is None:
                    self.__params = self.__idents_matching(
                        lambda x: x & DEF_PARAM)
                return self.__params

            def get_locals(self):
                if self.__locals is None:
                    locs = (LOCAL, CELL)

                    def test(x): return ((x >> SCOPE_OFF) & SCOPE_MASK) in locs

                    self.__locals = self.__idents_matching(test)
                return self.__locals

            def get_globals(self):
                if self.__globals is None:
                    glob = (GLOBAL_IMPLICIT, GLOBAL_EXPLICIT)

                    def test(x): return ((x >> SCOPE_OFF) & SCOPE_MASK) in glob

                    self.__globals = self.__idents_matching(test)
                return self.__globals

            def get_nonlocals(self):
                if self.__nonlocals is None:
                    self.__nonlocals = self.__idents_matching(
                        lambda x: x & DEF_NONLOCAL)
                return self.__nonlocals

            def get_frees(self):
                if self.__frees is None:
                    def is_free(x): return (
                                                   (x >> SCOPE_OFF) & SCOPE_MASK) == FREE

                    self.__frees = self.__idents_matching(is_free)
                return self.__frees

        class Class(SymbolTable):

            __methods = None

            def get_methods(self):
                if self.__methods is None:
                    d = {}
                    for st in self._table.children:
                        d[st.name] = 1
                    self.__methods = tuple(d)
                return self.__methods

        class Symbol(object):

            def __init__(self, name, flags, namespaces=None):
                self.__name = name
                self.__flags = flags
                # like PyST_GetScope()
                self.__scope = (flags >> SCOPE_OFF) & SCOPE_MASK
                self.__namespaces = namespaces or ()

            def __repr__(self):
                return "<symbol {0!r}>".format(self.__name)

            def get_name(self):
                return self.__name

            def is_referenced(self):
                return bool(self.__flags & _symtable.USE)

            def is_parameter(self):
                return bool(self.__flags & DEF_PARAM)

            def is_global(self):
                return bool(self.__scope in (GLOBAL_IMPLICIT, GLOBAL_EXPLICIT))

            def is_nonlocal(self):
                return bool(self.__flags & DEF_NONLOCAL)

            def is_declared_global(self):
                return bool(self.__scope == GLOBAL_EXPLICIT)

            def is_local(self):
                return bool(self.__scope in (LOCAL, CELL))

            def is_annotated(self):
                return bool(self.__flags & DEF_ANNOT)

            def is_free(self):
                return bool(self.__scope == FREE)

            def is_imported(self):
                return bool(self.__flags & DEF_IMPORT)

            def is_assigned(self):
                return bool(self.__flags & DEF_LOCAL)

            def is_namespace(self):
                """Returns true if name binding introduces new namespace.

                If the name is used as the target of a function or class
                statement, this will be true.

                Note that a single name can be bound to multiple objects.  If
                is_namespace() is true, the name may also be bound to other
                objects, like an int or list, that does not introduce a new
                namespace.
                """
                return bool(self.__namespaces)

            def get_namespaces(self):
                """Return a list of namespaces bound to this name"""
                return self.__namespaces

            def get_namespace(self):
                """Returns the single namespace bound to this name.

                Raises ValueError if the name is bound to multiple namespaces.
                """
                if len(self.__namespaces) != 1:
                    raise ValueError("name is bound to multiple namespaces")
                return self.__namespaces[0]

        if __name__ == "__main__":
            import os
            import sys
            with open(sys.argv[0]) as f:
                src = f.read()
            mod = symtable(src, os.path.split(sys.argv[0])[1], "exec")
            for ident in mod.get_identifiers():
                info = mod.lookup(ident)
                print(info, info.is_local(), info.is_namespace())

    # encoding: utf-8
    # module mmap
    # from /home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/mmap.cpython-39-x86_64-linux-gnu.so
    # by generator 1.147
    # no doc
    # no imports

    # Variables with simple values

    ACCESS_COPY = 3
    ACCESS_DEFAULT = 0
    ACCESS_READ = 1
    ACCESS_WRITE = 2

    ALLOCATIONGRANULARITY = 4096

    MADV_DOFORK = 11
    MADV_DONTFORK = 10
    MADV_DONTNEED = 4
    MADV_HWPOISON = 100
    MADV_MERGEABLE = 12
    MADV_NORMAL = 0
    MADV_RANDOM = 1
    MADV_REMOVE = 9
    MADV_SEQUENTIAL = 2
    MADV_UNMERGEABLE = 13
    MADV_WILLNEED = 3

    MAP_ANON = 32
    MAP_ANONYMOUS = 32
    MAP_DENYWRITE = 2048
    MAP_EXECUTABLE = 4096
    MAP_PRIVATE = 2
    MAP_SHARED = 1

    PAGESIZE = 4096

    PROT_EXEC = 4
    PROT_READ = 1
    PROT_WRITE = 2

    # no functions
    # classes

    class error(Exception):
        """ Base class for I/O related errors. """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*cls, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __str__(self, *args, **kwargs):  # real signature unknown
            """ Return str(self). """
            pass

        characters_written = property(lambda self: object(
        ), lambda self, v: None, lambda self: None)  # default

        errno = property(lambda self: object(), lambda self,
                                                       v: None, lambda self: None)  # default
        """POSIX exception code"""

        filename = property(lambda self: object(), lambda self,
                                                          v: None, lambda self: None)  # default
        """exception filename"""

        filename2 = property(lambda self: object(), lambda self,
                                                           v: None, lambda self: None)  # default
        """second exception filename"""

        strerror = property(lambda self: object(), lambda self,
                                                          v: None, lambda self: None)  # default
        """exception strerror"""

    class map:

        def close(self, *args, **kwargs):  # real signature unknown
            pass

        def find(self, *args, **kwargs):  # real signature unknown
            pass

        def flush(self, *args, **kwargs):  # real signature unknown
            pass

        def madvise(self, *args, **kwargs):  # real signature unknown
            pass

        def move(self, *args, **kwargs):  # real signature unknown
            pass

        def read(self, *args, **kwargs):  # real signature unknown
            pass

        def readline(self, *args, **kwargs):  # real signature unknown
            pass

        def read_byte(self, *args, **kwargs):  # real signature unknown
            pass

        def resize(self, *args, **kwargs):  # real signature unknown
            pass

        def rfind(self, *args, **kwargs):  # real signature unknown
            pass

        def seek(self, *args, **kwargs):  # real signature unknown
            pass

        def size(self, *args, **kwargs):  # real signature unknown
            pass

        def tell(self, *args, **kwargs):  # real signature unknown
            pass

        def write(self, *args, **kwargs):  # real signature unknown
            pass

        def write_byte(self, *args, **kwargs):  # real signature unknown
            pass

        def __delitem__(self, *args, **kwargs):  # real signature unknown
            """ Delete self[key]. """
            pass

        def __enter__(self, *args, **kwargs):  # real signature unknown
            pass

        def __exit__(self, *args, **kwargs):  # real signature unknown
            pass

        def __getattribute__(self, *args, **kwargs):  # real signature unknown
            """ Return getattr(self, name). """
            pass

        def __getitem__(self, *args, **kwargs):  # real signature unknown
            """ Return self[key]. """
            pass

        @staticmethod
        def __init__():  # real signature unknown; restored from __doc__
            pass

        def __len__(self, *args, **kwargs):  # real signature unknown
            """ Return len(self). """
            pass

        @staticmethod  # known case of __new__
        def __new__(*cls, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        def __setitem__(self, *args, **kwargs):  # real signature unknown
            """ Set self[key] to value. """
            pass

        closed = property(lambda self: object(), lambda self,
                                                        v: None, lambda self: None)  # default

    # variables with complex values

    # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f30e7863e80>'
    __loader__ = None

    __spec__ = None  # (!) real value is "ModuleSpec(name='mmap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f30e7863e80>, origin='/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/mmap.cpython-39-x86_64-linux-gnu.so')"

    @staticmethod
    def Resource():
        # encoding: utf-8
        # module resource
        # from /home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/resource.cpython-39-x86_64-linux-gnu.so
        # by generator 1.147
        # no doc
        # no imports

        # Variables with simple values

        # functions

        # classes

        class error(Exception):
            """ Base class for I/O related errors. """

            def __init__(self, *args, **kwargs):  # real signature unknown
                pass

            @staticmethod  # known case of __new__
            def __new__(*cls, **kwargs):  # real signature unknown
                """ Create and return a new object.  See help(type) for accurate signature. """
                pass

            def __reduce__(self, *args, **kwargs):  # real signature unknown
                pass

            def __str__(self, *args, **kwargs):  # real signature unknown
                """ Return str(self). """
                pass

            characters_written = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default

            errno = property(lambda self: object(), lambda self,
                                                           v: None, lambda self: None)  # default
            """POSIX exception code"""

            filename = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """exception filename"""

            filename2 = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """second exception filename"""

            strerror = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """exception strerror"""

        error()

        class struct_rusage(tuple):
            """
            struct_rusage: Result from getrusage.

            This object may be accessed either as a tuple of
                (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,
                nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)
            or via the attributes ru_utime, ru_stime, ru_maxrss, and so on.
            """

            def __init__(self, *args, **kwargs):  # real signature unknown
                pass

            @staticmethod  # known case of __new__
            def __new__(*cls, **kwargs):  # real signature unknown
                """ Create and return a new object.  See help(type) for accurate signature. """
                pass

            def __reduce__(self, *args, **kwargs):  # real signature unknown
                pass

            def __repr__(self, *args, **kwargs):  # real signature unknown
                """ Return repr(self). """
                pass

            ru_idrss = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """unshared data size"""

            ru_inblock = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """block input operations"""

            ru_isrss = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """unshared stack size"""

            ru_ixrss = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """shared memory size"""

            ru_majflt = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """page faults requiring I/O"""

            ru_maxrss = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """max. resident set size"""

            ru_minflt = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """page faults not requiring I/O"""

            ru_msgrcv = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """IPC messages received"""

            ru_msgsnd = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """IPC messages sent"""

            ru_nivcsw = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """involuntary context switches"""

            ru_nsignals = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """signals received"""

            ru_nswap = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """number of swap outs"""

            ru_nvcsw = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """voluntary context switches"""

            ru_oublock = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """block output operations"""

            ru_stime = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """system time used"""

            ru_utime = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """user time used"""

            n_fields = 16
            n_sequence_fields = 16
            n_unnamed_fields = 0

        struct_rusage()
        # variables with complex values

        # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f30e7863e80>'
        __loader__ = None

        __spec__ = None  # (!) real value is "ModuleSpec(name='resource', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f30e7863e80>, origin='/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/resource.cpython-39-x86_64-linux-gnu.so')"

    """Simple class to read IFF chunks.

    An IFF chunk (used in formats such as AIFF, TIFF, RMFF (RealMedia File
    Format)) has the following structure:

    +----------------+
    | ID (4 bytes)   |
    +----------------+
    | size (4 bytes) |
    +----------------+
    | data           |
    | ...            |
    +----------------+

    The ID is a 4-byte string which identifies the type of chunk.

    The size field (a 32-bit value, encoded using big-endian byte order)
    gives the size of the whole chunk, including the 8-byte header.

    Usually an IFF-type file consists of one or more chunks.  The proposed
    usage of the Chunk class defined here is to instantiate an instance at
    the start of each chunk and read from the instance until it reaches
    the end, after which a new instance can be instantiated.  At the end
    of the file, creating a new instance will fail with an EOFError
    exception.

    Usage:
    while True:
        try:
            chunk = Chunk(file)
        except EOFError:
            break
        chunktype = chunk.getname()
        while True:
            data = chunk.read(nbytes)
            if not data:
                pass
            # do something with data

    The interface is file-like.  The implemented methods are:
    read, close, seek, tell, isatty.
    Extra methods are: skip() (called by close, skips to the end of the chunk),
    getname() (returns the name (ID) of the chunk)

    The __init__ method has one required argument, a file-like object
    (including a chunk instance), and one optional argument, a flag which
    specifies whether or not chunks are aligned on 2-byte boundaries.  The
    default is 1, i.e. aligned.
    """

    class Chunk:
        def __init__(self, file, align=True, bigendian=True, inclheader=False):
            import struct
            self.closed = True
            self.align = align  # whether to align to word (2-byte) boundaries
            if bigendian:
                strflag = '>'
            else:
                strflag = '<'
            self.file = file
            self.chunkname = file.read(4)
            if len(self.chunkname) < 4:
                raise EOFError
            try:
                self.chunksize = struct.unpack_from(
                    strflag + 'L', file.read(4))[0]
            except struct.error:
                raise EOFError from None
            if inclheader:
                self.chunksize = self.chunksize - 8  # subtract header
            self.size_read = 0
            try:
                self.offset = self.file.tell()
            except (AttributeError, OSError):
                self.seekable = False
            else:
                self.seekable = True

        def getname(self):
            """Return the name (ID) of the current chunk."""
            return self.chunkname

        def getsize(self):
            """Return the size of the current chunk."""
            return self.chunksize

        def close(self):
            if not self.closed:
                try:
                    self.skip()
                finally:
                    self.closed = True

        def isatty(self):
            if self.closed:
                raise ValueError("I/O operation on closed file")
            return False

        def seek(self, pos, whence=0):
            """Seek to specified position into the chunk.
            Default position is 0 (start of chunk).
            If the file is not seekable, this will result in an error.
            """

            if self.closed:
                raise ValueError("I/O operation on closed file")
            if not self.seekable:
                raise OSError("cannot seek")
            if whence == 1:
                pos = pos + self.size_read
            elif whence == 2:
                pos = pos + self.chunksize
            if pos < 0 or pos > self.chunksize:
                raise RuntimeError
            self.file.seek(self.offset + pos, 0)
            self.size_read = pos

        def tell(self):
            if self.closed:
                raise ValueError("I/O operation on closed file")
            return self.size_read

        def read(self, size=-1):
            """Read at most size bytes from the chunk.
            If size is omitted or negative, read until the end
            of the chunk.
            """

            if self.closed:
                raise ValueError("I/O operation on closed file")
            if self.size_read >= self.chunksize:
                return b''
            if size < 0:
                size = self.chunksize - self.size_read
            if size > self.chunksize - self.size_read:
                size = self.chunksize - self.size_read
            data = self.file.read(size)
            self.size_read = self.size_read + len(data)
            if self.size_read == self.chunksize and \
                    self.align and \
                    (self.chunksize & 1):
                dummy = self.file.read(1)
                self.size_read = self.size_read + len(dummy)
            return data

        def skip(self):
            """Skip the rest of the chunk.
            If you are not interested in the contents of the chunk,
            this method should be called so that the file points to
            the start of the next chunk.
            """

            if self.closed:
                raise ValueError("I/O operation on closed file")
            if self.seekable:
                try:
                    n = self.chunksize - self.size_read
                    # maybe fix alignment
                    if self.align and (self.chunksize & 1):
                        n = n + 1
                    self.file.seek(n, 1)
                    self.size_read = self.size_read + n
                    return
                except OSError:
                    pass
            while self.size_read < self.chunksize:
                n = min(8192, self.chunksize - self.size_read)
                dummy = self.read(n)
                if not dummy:
                    raise EOFError

    @staticmethod
    def Graphlib():

        _NODE_OUT = -1
        _NODE_DONE = -2

        class _NodeInfo:
            __slots__ = "node", "npredecessors", "successors"

            def __init__(self, node):
                # The node this class is augmenting.
                self.node = node

                # Number of predecessors, generally >= 0. When this value falls to 0,
                # and is returned by get_ready(), this is set to _NODE_OUT and when the
                # node is marked done by a call to done(), set to _NODE_DONE.
                self.npredecessors = 0

                # List of successor nodes. The list can contain duplicated elements as
                # long as they're all reflected in the successor's npredecessors attribute).
                self.successors = []

        class CycleError(ValueError):
            """Subclass of ValueError raised by TopologicalSorterif cycles exist in the graph

            If multiple cycles exist, only one undefined choice among them will be reported
            and included in the exception. The detected cycle can be accessed via the second
            element in the *args* attribute of the exception instance and consists in a list
            of nodes, such that each node is, in the graph, an immediate predecessor of the
            next node in the list. In the reported list, the first and the last node will be
            the same, to make it clear that it is cyclic.
            """

            pass

        class TopologicalSorter:
            """Provides functionality to topologically sort a graph of hashable nodes"""

            def __init__(self, graph=None):
                self._node2info = {}
                self._ready_nodes = None
                self._npassedout = 0
                self._nfinished = 0

                if graph is not None:
                    for node, predecessors in graph.items():
                        self.add(node, *predecessors)

            def _get_nodeinfo(self, node):
                if (result := self._node2info.get(node)) is None:
                    self._node2info[node] = result = _NodeInfo(node)
                return result

            def add(self, node, *predecessors):
                """Add a new node and its predecessors to the graph.

                Both the *node* and all elements in *predecessors* must be hashable.

                If called multiple times with the same node argument, the set of dependencies
                will be the union of all dependencies passed in.

                It is possible to add a node with no dependencies (*predecessors* is not provided)
                as well as provide a dependency twice. If a node that has not been provided before
                is included among *predecessors* it will be automatically added to the graph with
                no predecessors of its own.

                Raises ValueError if called after "prepare".
                """
                if self._ready_nodes is not None:
                    raise ValueError(
                        "Nodes cannot be added after a call to prepare()")

                # Create the node -> predecessor edges
                nodeinfo = self._get_nodeinfo(node)
                nodeinfo.npredecessors += len(predecessors)

                # Create the predecessor -> node edges
                for pred in predecessors:
                    pred_info = self._get_nodeinfo(pred)
                    pred_info.successors.append(node)

            def prepare(self):
                """Mark the graph as finished and check for cycles in the graph.

                If any cycle is detected, "CycleError" will be raised, but "get_ready" can
                still be used to obtain as many nodes as possible until cycles block more
                progress. After a call to this function, the graph cannot be modified and
                therefore no more nodes can be added using "add".
                """
                if self._ready_nodes is not None:
                    raise ValueError("cannot prepare() more than once")

                self._ready_nodes = [
                    i.node for i in self._node2info.values() if i.npredecessors == 0
                ]
                # ready_nodes is set before we look for cycles on purpose:
                # if the user wants to catch the CycleError, that's fine,
                # they can continue using the instance to grab as many
                # nodes as possible before cycles block more progress
                cycle = self._find_cycle
                if cycle:
                    raise CycleError(f"nodes are in a cycle", cycle)

            def get_ready(self):
                """Return a tuple of all the nodes that are ready.

                Initially it returns all nodes with no predecessors; once those are marked
                as processed by calling "done", further calls will return all new nodes that
                have all their predecessors already processed. Once no more progress can be made,
                empty tuples are returned.

                Raises ValueError if called without calling "prepare" previously.
                """
                if self._ready_nodes is None:
                    raise ValueError("prepare() must be called first")

                # Get the nodes that are ready and mark them
                result = tuple(self._ready_nodes)
                n2i = self._node2info
                for node in result:
                    n2i[node].npredecessors = _NODE_OUT

                # Clean the list of nodes that are ready and update
                # the counter of nodes that we have returned.
                self._ready_nodes.clear()
                self._npassedout += len(result)

                return result

            def is_active(self):
                """Return True if more progress can be made and ``False`` otherwise.

                Progress can be made if cycles do not block the resolution and either there
                are still nodes ready that haven't yet been returned by "get_ready" or the
                number of nodes marked "done" is less than the number that have been returned
                by "get_ready".

                Raises ValueError if called without calling "prepare" previously.
                """
                if self._ready_nodes is None:
                    raise ValueError("prepare() must be called first")
                return self._nfinished < self._npassedout or bool(self._ready_nodes)

            def __bool__(self):
                return self.is_active()

            def done(self, *nodes):
                """Marks a set of nodes returned by "get_ready" as processed.

                This method unblocks any successor of each node in *nodes* for being returned
                in the future by a a call to "get_ready"

                Raises :exec:`ValueError` if any node in *nodes* has already been marked as
                processed by a previous call to this method, if a node was not added to the
                graph by using "add" or if called without calling "prepare" previously or if
                node has not yet been returned by "get_ready".
                """

                if self._ready_nodes is None:
                    raise ValueError("prepare() must be called first")

                n2i = self._node2info

                for node in nodes:

                    # Check if we know about this node (it was added previously using add()
                    if (nodeinfo := n2i.get(node)) is None:
                        raise ValueError(
                            f"node {node!r} was not added using add()")

                    # If the node has not being returned (marked as ready) previously, inform the user.
                    stat = nodeinfo.npredecessors
                    if stat != _NODE_OUT:
                        if stat >= 0:
                            raise ValueError(
                                f"node {node!r} was not passed out (still not ready)"
                            )
                        elif stat == _NODE_DONE:
                            raise ValueError(
                                f"node {node!r} was already marked done")
                        else:
                            assert False, f"node {node!r}: unknown status {stat}"

                    # Mark the node as processed
                    nodeinfo.npredecessors = _NODE_DONE

                    # Go to all the successors and reduce the number of predecessors, collecting all the ones
                    # that are ready to be returned in the next get_ready() call.
                    for successor in nodeinfo.successors:
                        successor_info = n2i[successor]
                        successor_info.npredecessors -= 1
                        if successor_info.npredecessors == 0:
                            self._ready_nodes.append(successor)
                    self._nfinished += 1
                TopologicalSorter()

            @property
            def _find_cycle(self):
                n2i = self._node2info
                stack = []
                itstack = []
                seen = set()
                node2stacki = {}

                for node in n2i:
                    if node in seen:
                        continue

                    while True:
                        if node in seen:
                            # If we have seen already the node and is in the
                            # current stack we have found a cycle.
                            if node in node2stacki:
                                return stack[node2stacki[node]:] + [node]
                            # else go on to get next successor
                        else:
                            seen.add(node)
                            itstack.append(iter(n2i[node].successors).__next__)
                            node2stacki[node] = len(stack)
                            stack.append(node)

                        # Backtrack to the topmost stack entry with
                        # at least another successor.
                        while stack:
                            try:
                                node = itstack[-1]()
                                break
                            except StopIteration:
                                del node2stacki[stack.pop()]
                                itstack.pop()
                        else:
                            break
                return None

            def static_order(self):
                """Returns an iterable of nodes in a topological order.

                The particular order that is returned may depend on the specific
                order in which the items were inserted in the graph.

                Using this method does not require to call "prepare" or "done". If any
                cycle is detected, :exc:`CycleError` will be raised.
                """
                self.prepare()
                while self.is_active():
                    node_group = self.get_ready()
                    yield from node_group
                    self.done(*node_group)

    @staticmethod
    def Pwd():
        # encoding: utf-8
        # module pwd
        # from (built-in)
        # by generator 1.147
        """
        This module provides access to the Unix password database.
        It is available on all Unix versions.

        Password database entries are reported as 7-tuples containing the following
        items from the password database (see `<pwd.h>'), in order:
        pw_name, pw_passwd, pw_uid, pw_gid, pw_gecos, pw_dir, pw_shell.
        The uid and gid items are integers, all others are strings. An
        exception is raised if the entry asked for cannot be found.
        """

        # no imports

        # functions

        def getpwall():  # real signature unknown
            """
            Return a list of all available password database entries, in arbitrary order.

            See help(pwd) for more on password database entries.
            """
            pass

        getpwall()

        def getpwnam():  # real signature unknown
            """
            Return the password database entry for the given user name.

            See `help(pwd)` for more on password database entries.
            """
            pass

        getpwnam()

        def getpwuid():  # real signature unknown
            """
            Return the password database entry for the given numeric user ID.

            See `help(pwd)` for more on password database entries.
            """
            pass

        getpwuid()

        class struct_passwd(tuple):
            """
            pwd.struct_passwd: Results from getpw*() routines.

            This object may be accessed either as a tuple of
              (pw_name,pw_passwd,pw_uid,pw_gid,pw_gecos,pw_dir,pw_shell)
            or via the object attributes as named in the above tuple.
            """

            def __init__(self, *args, **kwargs):  # real signature unknown
                pass

            @staticmethod  # known case of __new__
            def __new__(*cls, **kwargs):  # real signature unknown
                """ Create and return a new object.  See help(type) for accurate signature. """
                pass

            def __reduce__(self, *args, **kwargs):  # real signature unknown
                pass

            def __repr__(self, *args, **kwargs):  # real signature unknown
                """ Return repr(self). """
                pass

            pw_dir = property(lambda self: '')
            """home directory

            :type: string
            """

            pw_gecos = property(lambda self: '')
            """real name

            :type: string
            """

            pw_gid = property(lambda self: 0)
            """group id

            :type: int
            """

            pw_name = property(lambda self: '')
            """user name

            :type: string
            """

            pw_passwd = property(lambda self: '')
            """password

            :type: string
            """

            pw_shell = property(lambda self: '')
            """shell program

            :type: string
            """

            pw_uid: int = property(lambda self: 0)
            """user id

            :type: int
            """

            n_fields = 7
            n_sequence_fields = 7
            n_unnamed_fields = 0

        struct_passwd()

        class __loader__(object):
            """
            Meta path import for built-in modules.

                All methods are either class or static methods to avoid the need to
                instantiate the class.
            """

            @classmethod
            def create_module(cls, *args, **kwargs):  # real signature unknown
                """ Create a built-in module """
                pass

            @classmethod
            def exec_module(cls, *args, **kwargs):  # real signature unknown
                """ Exec a built-in module """
                pass

            @classmethod
            def find_module(cls, *args, **kwargs):  # real signature unknown
                """
                Find the built-in module.

                        If 'path' is ever specified then the search is considered a failure.

                        This method is deprecated.  Use find_spec() instead.
                """
                pass

            @classmethod
            def find_spec(cls, *args, **kwargs):  # real signature unknown
                pass

            @classmethod
            def get_code(cls, *args, **kwargs):  # real signature unknown
                """ Return None as built-in modules do not have code objects. """
                pass

            @classmethod
            def get_source(cls, *args, **kwargs):  # real signature unknown
                """ Return None as built-in modules do not have source code. """
                pass

            @classmethod
            def is_package(cls, *args, **kwargs):  # real signature unknown
                """ Return False as built-in modules are never packages. """
                pass

            @classmethod
            def load_module(cls, *args, **kwargs):  # real signature unknown
                """
                Load the specified module into sys.modules and return it.

                    This method is deprecated.  Use loader.exec_module instead.
                """
                pass

            def module_repr(self):  # reliably restored by inspect
                """
                Return repr for the module.

                        The method is deprecated.  The import machinery does the job itself.
                """
                pass

            def __init__(self, *args, **kwargs):  # real signature unknown
                pass

            __weakref__ = property(lambda self: object(
            ), lambda self, v: None, lambda self: None)  # default
            """list of weak references to the object (if defined)"""

            _ORIGIN = 'built-in'
            __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod object at 0x7f30e8110430>, 'find_spec': <classmethod object at 0x7f30e8110460>, 'find_module': <classmethod object at 0x7f30e8110490>, 'create_module': <classmethod object at 0x7f30e81104c0>, 'exec_module': <classmethod object at 0x7f30e81104f0>, 'get_code': <classmethod object at 0x7f30e8110580>, 'get_source': <classmethod object at 0x7f30e8110610>, 'is_package': <classmethod object at 0x7f30e81106a0>, 'load_module': <classmethod object at 0x7f30e81106d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"

        # variables with complex values
        __loader__()
        # (!) real value is "ModuleSpec(name='pwd', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"
        __spec__ = None

    class Runner(object):
        def __init__(self, method):
            import time
            self.name = "Runner"
            print("starting..")
            time.sleep(12)
            print(f"id : {id(method)}")
            try:
                method()

            except Exception as err:
                print(err)

            print("code finished")

    @staticmethod
    def forloop(number):
        for i in range(number):
            print(i)

    @staticmethod
    def Append(name, add):
        name.append(add)

    @staticmethod
    def Remove(name, R):
        name.remove(R)

    @staticmethod
    def sort(listname):
        listname.sort()

    @staticmethod
    def listitems(parameter_list):
        list = [parameter_list]

        print(list)

    @staticmethod
    def abort():
        print(os.abort())

    class NumburstoRupees:
        def __init__(self, number, add=0):
            self.number = number
            print("")
            print("$", number + add)
            print("")

    class animalsandhumantype:
        class Dog:
            def __init__(self, name, age):
                self.name = name
                self.age = age

                print("Bow hello my name is " + self.name + " and i am ",
                      self.age, " years old and i am a dog")

        class Cat:
            def __init__(self, name, age):
                self.name = name
                self.age = age

                print("Meow hello my name is " + self.name +
                      " and i am ", self.age, " years old and i am a Cat")

        class Rabbit:
            def __init__(self, name, age):
                self.name = name
                self.age = age

                print("hello my name is " + self.name + " and i am ",
                      self.age, " years old and i am a Rabbit")

        class Human:
            def __init__(self, name, age, city, country):
                self.name = name
                self.age = age
                self.city = city
                self.country = country

                print("hello my name is " + self.name + " and i am ", self.age,
                      " years old and i am a Rabbit and my city is " + self.city + " and my country is " + self.country)

    class RemoveDir:
        def __init__(self, Removedirname):
            import os
            os.remove(Removedirname)

    class exit:
        def __init__(self):
            import sys

            sys.exit()

    class Abort:
        def __init__(self):
            import os

            print(os.abort())

    class NewDir:
        def __init__(self, DirName):
            import os

            os.makedirs(DirName)

    @staticmethod
    def listdirs():
        import os

        print(os.listdir())

    @staticmethod
    def ctermid():
        print(os.ctermid())

    @staticmethod
    def cpu_count():
        print(os.cpu_count())

    @staticmethod
    def openpty():
        print(os.openpty())

    @staticmethod
    def mydrive():
        import webbrowser

        webbrowser.open_new("https://drive.google.com/drive/u/0/")

    @staticmethod
    def mail():
        import webbrowser

        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

    @staticmethod
    def __Dict__():
        try:
            Print = "{'__module__': '__main__', 'itertools': <module 'itertools' (built-in)>, 'importlib': <module 'importlib' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/importlib/__init__.py'>, 'collections': <module 'collections' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/collections/__init__.py'>, 'csv': <module 'csv' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/csv.py'>, 'math': <module 'math' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/math.cpython-39-x86_64-linux-gnu.so'>, 'json': <module 'json' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/json/__init__.py'>, 'datetime': <module 'datetime' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/datetime.py'>, 'turtle': <module 'turtle' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/turtle.py'>, 'random': <module 'random' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/random.py'>, 'system': <module 'os' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/os.py'>, 'jsys': <module 'sys' (built-in)>, 'email': <module 'email' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/email/__init__.py'>, 'calendar': <module 'calendar' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/calendar.py'>, 'time': <module 'time' (built-in)>, 'array': <module 'array' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/array.cpython-39-x86_64-linux-gnu.so'>, 'abc': <module 'abc' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/abc.py'>, 'easy_install': <module 'easy_install' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/site-packages/easy_install.py'>, 'i': <module 'itertools' (built-in)>, 'i1': <module 'importlib' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/importlib/__init__.py'>, 'i2': <module 'collections' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/collections/__init__.py'>, 'i3': <module 'csv' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/csv.py'>, 'i4': <module 'math' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/math.cpython-39-x86_64-linux-gnu.so'>, 'i5': <module 'json' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/json/__init__.py'>, 'i6': <module 'datetime' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/datetime.py'>, 'i7': <module 'turtle' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/turtle.py'>, 'i8': <module 'random' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/random.py'>, 'i9': <module 'os' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/os.py'>, 'i10': <module 'sys' (built-in)>, 'i11': <module 'email' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/email/__init__.py'>, 'i12': <module 'calendar' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/calendar.py'>, 'i13': <module 'time' (built-in)>, 'i14': <module 'array' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/lib-dynload/array.cpython-39-x86_64-linux-gnu.so'>, 'i15': <module 'abc' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/abc.py'>, 'i16': <module 'easy_install' from '/home/judsonleo/anaconda3/envs/judsonleo/lib/python3.9/site-packages/easy_install.py'>, 'Runner': <class '__main__.judson.Runner'>, 'forloop': <staticmethod object at 0x7fba6e3cab80>, 'Append': <staticmethod object at 0x7fba6e3d02b0>, 'Remove': <staticmethod object at 0x7fba6e3d0280>, 'sort': <staticmethod object at 0x7fba6e3d01f0>, 'listitems': <staticmethod object at 0x7fba6e3d0220>, 'abort': <staticmethod object at 0x7fba6dc909d0>, 'NumburstoRupees': <class '__main__.judson.NumburstoRupees'>, 'animalsandhumantype': <class '__main__.judson.animalsandhumantype'>, 'RemoveDir': <class '__main__.judson.RemoveDir'>, 'exit': <class '__main__.judson.exit'>, 'Abort': <class '__main__.judson.Abort'>, 'NewDir': <class '__main__.judson.NewDir'>, 'listdirs': <staticmethod object at 0x7fba6dc1f8e0>, 'ctermid': <staticmethod object at 0x7fba6dc1f940>, 'cpu_count': <staticmethod object at 0x7fba6dc1f970>, 'openpty': <staticmethod object at 0x7fba6dc1f640>, '__dict__': <attribute '__dict__' of 'judson' objects>, '__weakref__': <attribute '__weakref__' of 'judson' objects>, '__doc__': None}"
            print(Print)

        except Exception as err:
            print(err)

    @staticmethod
    def module():
        print("__main__")

    @staticmethod
    def weakrefoffset():
        print(24)

    @staticmethod
    def printAnyThingInTime(Print, Time):
        import time

        time.sleep(Time)
        print(Print)

    @staticmethod
    def bignumber(n1, n2):
        if n1 > n2:
            print("n1 is biggest number than n2")

        if n1 < n2:
            print("n2 is upper biggest number than n1")

    @staticmethod
    def BigString(s1, s2):
        if s1 > s2:
            print("s1 is biggest string than s2")
        if s1 < s2:
            print("s2 is upper biggest string than n1")


    class data:
        @staticmethod
        def storeStr(item):
            items = item
            print("StoreIng data...")
            import time
            time.sleep(4)
            print("StoredData " + items + " ...")

        @staticmethod
        def deleteStr(item):
            items = item

            print("Deleting data...")
            import time
            time.sleep(4)
            print("deleted " + items + " ...")

        @staticmethod
        def __add__(add):
            print("cannot add a data item with PROT_WRITER")

        @staticmethod
        def __mul__(mul):
            print("cannot mul a data item with PROT_WRITER")

        @staticmethod
        def __floordiv__(floordiv):
            print("cannot floordiv a data item with PROT_WRITER")

        @staticmethod
        def __floor__(floor):
            print("cannot floor a data item with PROT_WRITER")

        def __init__(self):
            print("")


if __name__ == '__main__':
    judson.data.__floor__(12)
