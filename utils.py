from colored import fg, attr


# Format print
def Print(content: str, color: str):
    print(fg(color) + content + attr("reset"))


# Check if the data is none
def isEmpty(content: str) -> bool:
    if content == "" or content == "\n\n":
        return False
    return True
