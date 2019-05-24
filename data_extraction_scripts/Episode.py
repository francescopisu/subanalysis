class Episode:
    id_ = 1
    length = 0
    wh = 0
    title = ""
    
    def __init__(self, id_=1, length=0, wh=0, title=""):
        self.id_ = id_
        self.length = length
        self.wh = wh
        self.title = title

    def __str__(self):
        return "Ep. " + str(self.id_) + \
            ", length: " + str(self.length) + \
            ", w/h: " + str(self.wh)  + \
            ", title: " + str(self.title)
