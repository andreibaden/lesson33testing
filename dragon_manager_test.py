import unittest

from dragon_manager import DragonManager


# AAA rule

class DragonManagerTest(unittest.TestCase):
    def test_negative_age(self):
        # arrange
        age = -1
        expected = 0

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_zero_age(self):
        # arrange
        age = 0
        expected = 0

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_string_age(self):
        # arrange
        age = "55"
        expected = 0

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_between_1_and_200(self):
        # arrange
        age = 100
        expected = 303

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_between_201_and_300(self):
        # arrange
        age = 250
        expected = 703

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_more_301_(self):
        # arrange
        age = 350
        expected = 853

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_with_1(self):
        # arrange
        age = 1
        expected = 6

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_with_200(self):
        # arrange
        age = 200
        expected = 603

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_with_201(self):
        # arrange
        age = 201
        expected = 605

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_with_300(self):
        # arrange
        age = 300
        expected = 803

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)

    def test_age_with_301(self):
        # arrange
        age = 301
        expected = 804

        # act
        actual = DragonManager.calculate_total_heads(age)

        # assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
