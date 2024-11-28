import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: ./ft_otp -g <key_file> or ./ft_otp -k <key_file>")
        return
    
    flag = sys.argv[1]
    if flag == "-g":
        pass
    elif flag == "-k":
        pass
    else:
        print("Invalid flag!!! Usage: ./ft_otp -g <key_file> or ./ft_otp -k <key_file>")
    
if __name__ == "__main__":
    main()