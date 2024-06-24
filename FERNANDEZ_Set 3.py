#!/usr/bin/env python
# coding: utf-8

# In[1]:


def relationship_status(from_member, to_member, social_graph):

    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"] :
        relationship = "friends"

    elif to_member in social_graph[from_member]["following"]:
        relationship = "follower"

    elif from_member in social_graph[to_member]["following"]:
        relationship = "followed by"

    else:
        relationship = "no relationship"

    return relationship


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

relationship_status("@joaquin", "@chums", social_graph)


# In[150]:


def tic_tac_toe(board):

    board_string = ""
    board_size = len(board)

    # checking for horizontal
    
    for i in range(0, board_size):

        if board[i].count("X") == board_size:
            return "X"
        elif  board[i].count("O") ==  board_size: 
            return "O"
        else:

            # checking for vertical
            
            for j in range(0, board_size):
                for i in range(0, board_size):
                    board_string += board[i][j]

                board_string += " "
    
            if ("X" * board_size) in board_string:
                return "X"
            elif ("O" * board_size) in board_string:
                return "O"
            else:

                # checking for diagonal (option 1)
                
                for i in range(0, board_size):
                    board_string += board[i][i]

                if ("X" * board_size) in board_string:
                    return "X"
                elif ("O" * board_size) in board_string:
                    return "O"
                else:

                    # checking for diagonal (option 2)
                    
                    for i in range(0, board_size):
                        j = board_size - 1 - i
                        board_string += board[i][j]

                    if ("X" * board_size) in board_string:
                        return "X"
                    elif ("O" * board_size) in board_string:
                        return "O"
                    else:
                        return "NO WINNER"

                

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

tic_tac_toe(board7)


# In[11]:


def eta(first_stop, second_stop, route_map):

    travel_time = 0

    while first_stop != second_stop:
        for (start, end), travel_info in route_map.items():
            if start == first_stop:
                travel_time += travel_info["travel_time_mins"]
                first_stop = end
                break
                
    return travel_time

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

eta("upd","dlsu",legs)

