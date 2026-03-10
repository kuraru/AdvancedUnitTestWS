"""
Temperature Converter util functions
"""
import asyncio


async def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


async def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


async def fahrenheit_to_celsius_array(fahrenheit_array):
    res = []
    for f in fahrenheit_array:
        res.append(await fahrenheit_to_celsius(f))
    return res


async def celsius_to_fahrenheit_array(celsius_array):
    res = []
    for c in celsius_array:
        res.append(await celsius_to_fahrenheit(c))
    return res


async def fahrenheit_to_celsius_rounded(fahrenheit):
    return round(
        await fahrenheit_to_celsius(fahrenheit), 2
    )


async def celsius_to_fahrenheit_rounded(celsius):
    return round(
        await celsius_to_fahrenheit(celsius), 2
    )


async def fahrenheit_to_celsius_array_rounded(fahrenheit_array):
    res = []
    for f in fahrenheit_array:
        res.append(await fahrenheit_to_celsius_rounded(f))
    return res


async def celsius_to_fahrenheit_array_rounded(celsius_array):
    res = []
    for c in celsius_array:
        res.append(await celsius_to_fahrenheit_rounded(c))
    return res
