from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Calculator")

# Addition tool
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

# Subtraction tool
@mcp.tool()
def sub(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b

# Multiplication tool
@mcp.tool()
def mul(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# Division tool
@mcp.tool()
def div(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Run the server
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')