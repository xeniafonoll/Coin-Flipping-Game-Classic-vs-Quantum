
import random

def run_classical_game_turn(computer_strategy_1, player_choice, computer_strategy_2):
    # Initial state: Tail (0)
    coin_state = 0  
    
    # Turn 1: Computer's choice (Flips or keeps)
    if computer_strategy_1 == 'flip':
        coin_state = 1 - coin_state
        
    # Turn 2: Player's choice (Flips or keeps)
    if player_choice == 'flip':
        coin_state = 1 - coin_state
        
    # Turn 3: Computer's choice (Flips or keeps)
    if computer_strategy_2 == 'flip':
        coin_state = 1 - coin_state
        
    return coin_state

def simulate_classical_trials(num_trials=100000):
    computer_wins = 0
    player_wins = 0
    
    strategies = ['keep', 'flip']
    
    for _ in range(num_trials):
        # In a classical environment, choices are governed by uniform random choices (stochastic)
        c1 = random.choice(strategies)
        p = random.choice(strategies)
        c2 = random.choice(strategies)
        
        final_state = run_classical_game_turn(c1, p, c2)
        
        # If final state is Head (1), Computer wins. If Tail (0), Player wins.
        if final_state == 1:
            computer_wins += 1
        else:
            player_wins += 1
            
    print(f"--- Classical Simulation Results ({num_trials} trials) ---")
    print(f"Computer Win Rate : {computer_wins / num_trials * 100:.2f}%")
    print(f"Player Win Rate   : {player_wins / num_trials * 100:.2f}%")

if __name__ == "__main__":
    simulate_classical_trials()
