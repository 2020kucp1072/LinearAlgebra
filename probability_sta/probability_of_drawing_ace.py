
'''
    @Author: VEMULA DILEEP
    @Date: 15-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 15-11-2024
    @Title : probability of drawing an ace

'''



def probability_of_drawing_ace():
    """
    Description:
    
    Calculate the probability of drawing an ace from a standard deck of cards.
    
    Returns:
        float: Probability of drawing an ace.
    """
    total_cards = 52
    aces = 4
    return aces / total_cards

def main():
    prob = probability_of_drawing_ace()
    print(f"Probability of drawing an ace: {prob}")

if __name__ == "__main__":
    main()
