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

file_content = """
Ala
ma
kota"""

@pytest.mark.asyncio
async def test_CM():
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        with AsyncFile("test_file") as f:
            assert isinstance(f, contextlib.AbstractAsyncContextManager)

## asyncio.iscoroutinefunction
