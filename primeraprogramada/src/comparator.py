class PlayComparator:
    def compare(self, a, b):
        if a.date < b.date: return -1
        if a.date > b.date: return 1
        
        if a.qtr < b.qtr: return -1
        if a.qtr > b.qtr: return 1
        
        if a.yards < b.yards: return -1
        if a.yards > b.yards: return 1
        
        if a.time < b.time: return -1
        if a.time > b.time: return 1
        
        return 0