import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        words = file.read().splitlines()
    filtered_words = filter(lambda x: len(x) > 3, words)
    with open(args.filename + '.new', 'w') as file:
        words = file.write('\n'.join(filtered_words))
    

if __name__ == '__main__':
    main()
