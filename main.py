import random

def main():
    """print randomly generated axes for Matt"""
    team1 = [str(i) for i in random.sample(list(range(0, 10)), 10)]
    team2 = [str(i) for i in random.sample(list(range(0, 10)), 10)]
    print('  ' + ' '.join(team1))
    print('\n'.join(team2))


if __name__ == '__main__':
    main()