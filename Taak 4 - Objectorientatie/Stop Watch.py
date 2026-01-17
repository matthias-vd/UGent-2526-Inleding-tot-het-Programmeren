class StopWatch:
    def __init__(self):
        self.sat=time.time()
        self.sot=time.time()
    def start(self):
        self.sat=time.time()
    def stop(self):
        self.sot=time.time()
    def get_start_time(self):
        return self.sat
    def get_end_time(self):
        return self.sot
    def get_elapsed_time(self):
        return int(self.sot-self.sat)