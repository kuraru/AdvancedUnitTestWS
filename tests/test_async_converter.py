import unittest


from AsyncConverterLib.async_converter import (
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius_array,
    celsius_to_fahrenheit_array,
    fahrenheit_to_celsius_rounded,
    celsius_to_fahrenheit_rounded,
    fahrenheit_to_celsius_array_rounded,
    celsius_to_fahrenheit_array_rounded,
)


class TestConverter(unittest.IsolatedAsyncioTestCase):
    async def test_fahrenheit_to_celsius_freezing_point(self):
        result = await fahrenheit_to_celsius(32)
        self.assertEqual(result, 0)

    async def test_fahrenheit_to_celsius_boiling_point(self):
        result = await fahrenheit_to_celsius(212)
        self.assertEqual(result, 100)

    async def test_celsius_to_fahrenheit_freezing_point(self):
        result = await celsius_to_fahrenheit(0)
        self.assertEqual(result, 32)

    async def test_celsius_to_fahrenheit_boiling_point(self):
        result = await celsius_to_fahrenheit(100)
        self.assertEqual(result, 212)

    async def test_fahrenheit_to_celsius_rounded(self):
        result = await fahrenheit_to_celsius_rounded(100)
        self.assertEqual(result, 37.78)

    async def test_celsius_to_fahrenheit_rounded(self):
        result = await celsius_to_fahrenheit_rounded(37.78)
        self.assertEqual(result, 100.0)

    async def test_fahrenheit_to_celsius_array(self):
        result = await fahrenheit_to_celsius_array([32, 212, 98.6])
        self.assertEqual(result, [0, 100, 37.0])

    async def test_celsius_to_fahrenheit_array(self):
        result = await celsius_to_fahrenheit_array([0, 100, 37])
        self.assertEqual(result, [32, 212, 98.6])

    async def test_fahrenheit_to_celsius_array_rounded(self):
        result = await fahrenheit_to_celsius_array_rounded([32, 100, 212])
        self.assertEqual(result, [0.0, 37.78, 100.0])

    async def test_celsius_to_fahrenheit_array_rounded(self):
        result = await celsius_to_fahrenheit_array_rounded([0, 37.78, 100])
        self.assertEqual(result, [32.0, 100.0, 212.0])

    async def test_empty_fahrenheit_array(self):
        result = await fahrenheit_to_celsius_array([])
        self.assertEqual(result, [])

    async def test_empty_celsius_array(self):
        result = await celsius_to_fahrenheit_array([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
