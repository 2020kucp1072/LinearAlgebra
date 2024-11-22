'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : probability of drawing an ace

'''


def probability_after_king():
    """
    Description:
    
    Calculate the probability of drawing an ace after a king is drawn (without replacement).
    
    Returns:
        float: Probability of drawing an ace after a king.
    """
    total_cards = 52
    aces = 4
    kings = 4
    return aces / (total_cards - 1)

def main():
    prob = probability_after_king()
    print(f"Probability of drawing an ace after a king: {prob}")

if __name__ == "__main__":
    main()
