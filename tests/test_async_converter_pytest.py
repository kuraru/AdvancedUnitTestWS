import pytest
import sys
import os

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

@pytest.mark.asyncio
async def test_fahrenheit_to_celsius_freezing_point():
    result = await fahrenheit_to_celsius(32)
    assert result == 0

@pytest.mark.asyncio
async def test_fahrenheit_to_celsius_boiling_point():
    result = await fahrenheit_to_celsius(212)
    assert result == 100

@pytest.mark.asyncio
async def test_celsius_to_fahrenheit_freezing_point():
    result = await celsius_to_fahrenheit(0)
    assert result == 32

@pytest.mark.asyncio
async def test_celsius_to_fahrenheit_boiling_point():
    result = await celsius_to_fahrenheit(100)
    assert result == 212

@pytest.mark.asyncio
async def test_fahrenheit_to_celsius_rounded():
    result = await fahrenheit_to_celsius_rounded(100)
    assert result == 37.78

@pytest.mark.asyncio
async def test_celsius_to_fahrenheit_rounded():
    result = await celsius_to_fahrenheit_rounded(37.78)
    assert result == 100.0

@pytest.mark.asyncio
async def test_fahrenheit_to_celsius_array():
    result = await fahrenheit_to_celsius_array([32, 212, 98.6])
    assert result == [0, 100, 37.0]

@pytest.mark.asyncio
async def test_celsius_to_fahrenheit_array():
    result = await celsius_to_fahrenheit_array([0, 100, 37])
    assert result == [32, 212, 98.6]

@pytest.mark.asyncio
async def test_fahrenheit_to_celsius_array_rounded():
    result = await fahrenheit_to_celsius_array_rounded([32, 100, 212])
    assert result == [0.0, 37.78, 100.0]

@pytest.mark.asyncio
async def test_celsius_to_fahrenheit_array_rounded():
    result = await celsius_to_fahrenheit_array_rounded([0, 37.78, 100])
    assert result == [32.0, 100.0, 212.0]

@pytest.mark.asyncio
async def test_empty_fahrenheit_array():
    result = await fahrenheit_to_celsius_array([])
    assert result == []

@pytest.mark.asyncio
async def test_empty_celsius_array():
    result = await celsius_to_fahrenheit_array([])
    assert result == []
