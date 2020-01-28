import random

def main():
    """print randomly generated axes for Matt"""
    team1 = [str(random.randint(0, 9)) for i in range(10)]
    team2 = [str(random.randint(0, 9)) for i in range(10)]
    print(', '.join(team1))
    print('\n'.join(team2))


if __name__ == '__main__':
    main()