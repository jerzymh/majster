class EnhancerBase:
    def enhance(self, signal):
        raise NotImplementedError 
    def unenhance(self, signal):
        raise NotImplementedError
    def __repr__(self):
        raise NotImplementedError
    pass