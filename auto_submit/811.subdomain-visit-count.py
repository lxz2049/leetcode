from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visits = Counter()
        for cpdomain in cpdomains:
            hits, domain = cpdomain.split(" ")
            comps = domain.split(".")
            for i in xrange(len(comps)):
                visits[".".join(comps[i:])] += int(hits)

        return ["%s %s" % (domain, hits) for hits, domain in visits.iteritems()]

    def test(self):
        print self.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
