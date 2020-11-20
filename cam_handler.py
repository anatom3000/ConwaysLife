class CameraHandler:
    def __init__(self, resolution, zoom=1.0, camera_pos=(0, 0)):
        self.resolution = resolution
        self.zoom = zoom
        self.camera_pos = camera_pos

    def home(self):
        self.camera_pos = (0, 0)
        self.zoom = 1.0

    def move_camera(self, x, y):
        self.camera_pos = (
            self.camera_pos[0] + x,
            self.camera_pos[1] + y,
        )

    def zoom_in(self, delta):
        self.zoom *= delta

    def zoom_out(self, delta):
        self.zoom /= delta

    def convert_pos(self, pos):
        return [
            pos[0] * self.zoom + self.resolution[0] / 2 - self.camera_pos[0],
            pos[1] * self.zoom + self.resolution[1] / 2 - self.camera_pos[1]
        ]
        # was
        # return [
        #             pos[0] * self.zoom + self.resolution[0] - self.camera_pos[0],
        #             pos[1] * self.zoom + self.resolution[1] - self.camera_pos[1]
        #         ]

    def convert_radius(self, radius):
        return radius * self.zoom

