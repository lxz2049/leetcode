class Solution(object):
    def __init__(self):
        self.ips = dict() # {ip: {timestamp: count}}
        self.buf = [set() for _ in xrange(1000)] # [{ip...}...]
        self.timestamp = [i for i in xrange(1000)]

    def send(self, ip, t):
        print "sending %s at %s" % (ip ,t)
        ts, ips = self.timestamp[t % 1000], self.buf[t % 1000]
        if ts != t:
            # evict
            for p in ips:
                self.ips[p].pop(ts)
                if not self.ips[p]:
                    self.ips.pop(p)
            self.buf[t % 1000].clear()
            self.timestamp[t % 1000] = t
            
        # get count
        print self.ips.get('a'), self.ips.get('b'), self.buf[:5], self.timestamp[:5]
        count = sum(self.ips.get(ip, dict()).itervalues())
        if count > 2:
            return False
        
        # add
        self.buf[t % 1000].add(ip)
        if ip not in self.ips:
            self.ips[ip] = dict()
        if ts not in self.ips[ip]:
            self.ips[ip][t] = 0
        self.ips[ip][t] += 1
        return True

    def test(self):
        print self.send("a", 0)
        print self.send("b", 0)
        print self.send("a", 1)
        print self.send("b", 1)
        print self.send("a", 2)
        print self.send("b", 2)
        print self.send("a", 3)
        print self.send("b", 3)
        print self.send("a", 1000)
        print self.send("a", 1001)
        print self.send("a", 1002)
        print self.send("a", 1003)
