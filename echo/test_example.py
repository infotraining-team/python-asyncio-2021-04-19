import pytest
import asyncio

async def adder(a, b):
    return a + b

@pytest.mark.asyncio
async def test_adder():
    res = await adder(3, 4)
    assert res == 7