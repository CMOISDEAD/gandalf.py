from colored import fg, attr


# Format print
def Print(content: str, color: str):
    print(fg(color) + content + attr("reset"))
