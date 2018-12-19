"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:

    BUFFERSIZE = 4

    def __init__(self):
        self.buf = [None] * self.BUFFERSIZE
        self.head = self.tail = 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        totalRead = (self.tail - self.head) % self.BUFFERSIZE
        buf[:totalRead] = self.buf[self.head:self.tail]
        self.head = self.tail = 0

        while totalRead < n:
            bytesRead = Reader.read4(self.buf)
            if not bytesRead:
                break
            self.tail = bytesRead
            bytesToWrite = min(n-totalRead, bytesRead)
            buf[totalRead:totalRead+bytesToWrite] = self.buf[:bytesToWrite]
            totalRead += bytesToWrite
            self.head = bytesToWrite

        return totalRead

