from django.test import TestCase


class MetaTests(TestCase):
    def test_meta(self):
        self.assertEqual(True, True)

    def test_antimeta(self):
        self.assertEqual(False, False)
