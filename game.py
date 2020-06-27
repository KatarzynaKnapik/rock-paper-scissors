# logic

import random

def game_start():
    users_name = input('Enter your name:')
    print('Hello, {}'.format(users_name))
    rating = open('rating.txt', 'r+')
    score = 0
    if users_name not in rating:
       print('\n'+users_name, int(score), sep=" ", end="\n", file=rating)
    
    rating.close()
    return users_name

def read_game_possibilities(user_input):
    game_possibilities = user_input.split(',')
    print("Okay, let's start")
    return game_possibilities

     
def read_rating(users_name):
    rating = open('rating.txt', 'r')
    score = 0
    for line in rating:
        elements = line.split(' ')
        if elements[0] == users_name:
            score = elements[1]
    
    rating.close()
    print('Your rating: {}'.format(score) )
    return int(score)

def convert_file():
    rating = open('rating.txt', 'r')
    scores = {}
    
    for line in rating:
        k, v = line.strip().split(' ')
        scores[k.strip()] = v.strip()
    rating.close()
    return scores

def update_score(users_name, game_output, scores):  
    
    for key in scores:
        s = int(scores[key])
        if key == users_name:
            if game_output == 'Win':
                scores[key] = s + 100
            elif game_output == 'Draw':
                scores[key] = s + 50
            elif game_output == 'Lose':
                scores[key] = s + 0
            
    rating = open('rating.txt', 'w')
    for key in scores:        
        print(key, scores[key], sep=" ", end="\n", file=rating)
    
    rating.close()
    
 
def proceed_game(users_name, user_input, user_game_possibilities):
    possible_inputs = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
    winning_config = {'rock':possible_inputs[1:8],
                      'fire':possible_inputs[2:9],
                      'scissors': possible_inputs[3:10],
                      'snake': possible_inputs[4:11],
                      'human': possible_inputs[5:12],
                      'tree': possible_inputs[6:13],
                      'wolf': possible_inputs[7: 14],
                      'sponge': possible_inputs[8:15],
                      'paper': possible_inputs[9:16],
                      'air': possible_inputs[10:17],
                      'water': possible_inputs[11:18],
                      'dragon': possible_inputs[12:19],
                      'devil': possible_inputs[13:20],
                      'lightning': possible_inputs[14:21],
                      'gun': possible_inputs[15:22]
                      }
    output = {"Lose": "Sorry, but computer chose {}", "Draw":"There is a draw ({})", "Win":"Well done. Computer chose {} and failed"}
    computer = user_game_possibilities
    game_output = ''
    
    index = random.randint(0, len(computer) - 1)

    if len(user_game_possibilities) == 1 and user_game_possibilities[0] == '':
        computer = ['rock', 'paper', 'scissors']
        index = random.randint(0, 2)

    if user_input in computer:
        if computer[index] in winning_config[user_input]:
            print(output["Win"].format(computer[index]))
            game_output = 'Win'
        elif computer[index] in user_input:
            print(output["Draw"].format(user_input))
            game_output = 'Draw'
        elif computer[index] not in winning_config[user_input]:
            print(output["Lose"].format(computer[index]))  
            game_output = 'Lose'
    elif user_input == "!exit":
        print("Bye!")
        return "Bye"
    elif user_input == '!rating':
        read_rating(users_name)
    else:
        print("Invalid input")
        
    return game_output
    
                   
                
        
# game  
  
users_name = game_start()
user_game_possibilities = input()
game_possiblities_arr = read_game_possibilities(user_game_possibilities)
while True:
    user_input = input()
    game_output = proceed_game(users_name, user_input, game_possiblities_arr)
    if game_output == "Bye":
        break
    scores = convert_file()
    update_score(users_name, game_output, scores)

    
        
