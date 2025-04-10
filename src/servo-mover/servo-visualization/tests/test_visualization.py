import unittest
from src.visualization.gui import GUI
from src.visualization.renderer import Renderer

class TestVisualization(unittest.TestCase):

    def setUp(self):
        self.gui = GUI()
        self.renderer = Renderer()

    def test_gui_initialization(self):
        self.assertIsNotNone(self.gui)
        self.assertTrue(self.gui.is_initialized())

    def test_renderer_initialization(self):
        self.assertIsNotNone(self.renderer)
        self.assertTrue(self.renderer.load_model("resources/models/arm_model.obj"))

    def test_update_display(self):
        self.gui.update_display(0, 0, 0)
        self.assertTrue(self.gui.display_updated)

    def test_render_arm_position(self):
        self.renderer.update_position(45, 90, 135)
        self.assertEqual(self.renderer.current_position, (45, 90, 135))

if __name__ == '__main__':
    unittest.main()