import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.splitlines()

    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if lines and all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if lines and all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered_items = [re.match(r"^(\d+)\. ", line) for line in lines]
    if lines and all(ordered_items):
        numbers = [int(item.group(1)) for item in ordered_items]
        if numbers == list(range(1, len(numbers) + 1)):
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
