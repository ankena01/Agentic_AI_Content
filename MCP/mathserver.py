from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Math')

@mcp.tool
def add(a:int , b:int) -> int:
    '''It will add two numbers'''
    return a+b 

@mcp.tool
def multiply(a:int , b:int) -> int:
    '''It will multiply two numbers'''
    return a*b 

if __name__ == '__main__':
    mcp.run(transport='stdio')