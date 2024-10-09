"""The module `pldf` provides some common utilities for Polars DataFrames when
exploring them with Jupyter notebooks.

Overview of functions:

    build_md: Builds a markdown string for the provided dataframe.
    build_schema: Builds a properly formatted string of the schema for the
                  provided dataframe
    print_md: Prints a dataframe as markdown to STDOUT, or otherwise defined by
              `file`
    print_schmea: Prints the schema of the dataframe to STDOUT, or otherwise
                  defined by `file`
    
"""

import sys
import polars as pl


def build_md(df: pl.DataFrame) -> str:
    """Convert a dataframe to a markdown string.
    
    Args:
        df (pl.DataFrame): The dataframe to be converted

    Returns:
        str: The dataframe formatted as markdown
    """
    # Get the header
    header = df.columns
    # Get the rows
    rows = df.rows()

    # Create Markdown table
    markdown = "| " + " | ".join(header) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(header)) + " |\n"
    for row in rows:
        markdown += "| " + " | ".join(map(str, row)) + " |\n"

    return markdown


def build_schema(schema: pl.Schema, indent=4, level=0, as_tree: bool = False):
    s = ""

    if level == 0 and as_tree:
        s += "root\n"
        s += build_schema(schema, indent=indent, level=1, as_tree=True)
        return s

    if as_tree:
        per_indent = "|" + " " * (indent - 1)
        indent_str = per_indent * (level - 1) + "|- "
    else:
        indent_str = " " * indent * level

    for field in schema:
        field_type = schema[field]
        if isinstance(field_type, pl.Struct):
            s += f"{indent_str}{field}: Struct\n"
            s += build_schema(
                field_type.to_schema(),
                indent=indent,
                level=level+1,
                as_tree=as_tree,
            )
        else:
            s += f"{indent_str}{field}: {field_type}\n"
            
    return s


def print_md(df: pl.DataFrame, file=sys.stdout):
    for l in build_md(df).splitlines():
        print(l, file=file)
        
def print_schema(schema: pl.Schema, indent=4, as_tree: bool = False, file=sys.stdout):
    for l in build_schema(schema, indent=indent, as_tree=as_tree).splitlines():
        print(l, file=file)
