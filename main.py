def getMultilineInput() -> list[str]:
    print('Please insert your data, when done use [Ctrl + D] shortcut')
    lines = []
    while True:
        try:
            params = input()
            
        except EOFError:
            break
        
        lines.append(params)
    
    return lines


if __name__ == '__main__':
    usr_data = getMultilineInput()
    