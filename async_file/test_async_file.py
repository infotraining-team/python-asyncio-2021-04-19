import pytest
import asyncio
from async_file import AsyncFile
import contextlib
import unittest.mock as mock

"""
with AsyncFile("filename.txt") as f:
    ## non-blocking read
    text = await f.readall()
    ## closing file
"""

file_content = """Ala
ma
kota"""

@pytest.mark.asyncio
async def test_CM():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        async with AsyncFile("test_file") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)

## asyncio.iscoroutinefunction readall
@pytest.mark.asyncio
async def test_readall():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        async with AsyncFile("test_file") as f:
            assert asyncio.iscoroutinefunction(f.readall)

## test file content
@pytest.mark.asyncio
async def test_readall_content():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        async with AsyncFile("test_file") as f:
            res = await f.readall()
            assert res == file_content

## iteration through lines
@pytest.mark.asyncio
async def test_readall_content():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        res = []
        async with AsyncFile("test_file") as f:
            async for line in f:
                res.append(line.strip())
        assert res == file_content.split()
