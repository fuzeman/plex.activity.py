0.7.0 (2016-09-06)
------------------
**Added**
 - :code:`Activity.start()` method now accepts a list of "sources" to use

**Changed**
 - Reduced severity of some common logger messages
 - Logging
     - Updated path hints for FreeBSD and FreeNAS
     - Updated activity parser patterns

0.6.2 (2015-02-05)
------------------
**Changes**
 - Wrap activity threads to catch any exceptions
 - [logging] implemented automatic path discovery
 - [logging] added path hint for QNAP TS-219P
 - [logging] added path hint for FreeNAS 9.3
 - [logging] updated messages/exceptions when "Plex Media Server.log" can't be found

**Fixed**
 - Python 3.x compatibility issues
 - [logging] catch reader/file close() exceptions (already closed, etc..)

0.6.1 (2015-01-04)
------------------
 - Added support for authentication tokens
 - Added Darwin/OSX "Plex Media Server.log" path hint
 - Fixes for Python 3+ comparability

0.6.0 (2014-10-30)
------------------
 - Initial release
