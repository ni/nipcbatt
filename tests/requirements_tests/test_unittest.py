"""This module provides unit tests framework check."""

import unittest


class TestUnittest(unittest.TestCase):
    """Defines a test fixture that checks unit test framework is ready to use.

    Args:
        unittest (unittest.TestCase): test case type
    """

    def setUp(self):
        print("Setup test fixture")

    def tearDown(self):
        print("Teardown fixture")

    def test_assert_equal(self):
        """Checks method unittest.TestCase.assertEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        expected = "str"
        actual = str("str")

        self.assertEqual(first=expected, second=actual)

    def test_assert_almost_equal(self):
        """Checks method unittest.TestCase.assertAlmostEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
        expected = 5
        actual = 5.1

        self.assertAlmostEqual(first=expected, second=actual, delta=0.1)

    def test_assert_assert_count_equal(self):
        """Checks method unittest.TestCase.assertCountEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (189 > 100 characters) (auto-generated noqa)
        expected = [1, 2, 3, 4]
        actual = reversed(expected)

        self.assertCountEqual(first=expected, second=actual)

    def test_assert_sequence_equal(self):
        """Checks method unittest.TestCase.assertSequenceEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        expected = [1, 2, 3, 4]
        actual = (1, 2, 3, 4)

        self.assertSequenceEqual(seq1=expected, seq2=actual)

    def test_assert_dict_equal(self):
        """Checks method unittest.TestCase.assertDictEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        dictionary_src = {"k1": "v1", "k2": "v2"}

        self.assertDictEqual(d1=dictionary_src, d2=dictionary_src)

    def test_assert_in(self):
        """Checks method unittest.TestCase.assertIn is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
        self.assertIn(member=2, container=(1, 2, 3))

    def test_assert_not_in(self):
        """Checks method unittest.TestCase.assertNotIn is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        self.assertNotIn(member=4, container=(1, 2, 3))

    def test_assert_is_not_none(self):
        """Checks method unittest.TestCase.assertIsNotNone is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        self.assertIsNotNone(obj={})

    def test_assert_is_none(self):
        """Checks method unittest.TestCase.assertIsNotNone is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        self.assertIsNone(obj=None)


if __name__ == "__main__":
    unittest.main()
