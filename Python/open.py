# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()

try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")