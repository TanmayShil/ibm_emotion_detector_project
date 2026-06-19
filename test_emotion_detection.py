import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

if __name__ == "__main__":
    unittest.main()
