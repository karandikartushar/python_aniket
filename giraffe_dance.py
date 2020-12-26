class giraffes():
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_back(self):
        print('right foot back')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
reginald=giraffes()
reginald.dance()
