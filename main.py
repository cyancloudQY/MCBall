from monte_carlo_simulation import *

def main():
    file = input('Enter the file that contains the coordinates: ')
    ball_info, ball_number = parse_input_file(file)
    back_ground_info = find_optimal_background(ball_info)

    num_of_simulation = int(input('Enter the number of simulated points: '))
    Monte_Carlo_result = Monte_Carlo_technique(ball_info, back_ground_info, num_of_simulation)

    print('When considering',num_of_simulation, 'number of simulated points, the volume calculated from Monte Carlo Simulation is', Monte_Carlo_result)

main()