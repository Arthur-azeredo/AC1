def anobi(ano):
    if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
        return True
    else:
        return False
    
def main():
    print(anobi(700))

main()