a_int=5
b_int=3
if a_int > b_int:
    print('a_int is larger than b_int')
else:
    print('b_int is larger than a_int')

team1_points = int(input('Enter team 1\'s points: '))
team2_points = int(input('Enter team 2\'s points: '))
if team1_points != team2_points:
    time_left = float(input('Enter time left in minutes: '))
    team_ball = int(input('Which team has the ball (1 or 2): '))
    time_left *= 60
    if team1_points > team2_points:
        points_ahead = team1_points - team2_points
    else:
        points_ahead = team2_points - team1_points
    points_ahead -=3
    if team1_points > team2_points:
        if team_ball == 1:
            points_ahead += .5
        else:
            points_ahead -= .5
    else:
        if team_ball == 2:
            points_ahead += .5
        else:
            points_ahead -= .5
    points_squared = points_ahead**2
    if points_squared > time_left:
        if team1_points > team2_points:
            print('Team 1\'s lead of ',team1_points-team2_points,' is safe')
        else:
            print('Team 2\'s lead of ',team2_points-team1_points,' is safe')
    else:
        if team1_points > team2_points:
            print('Team 1\'s lead of ',team1_points-team2_points,' is not safe')
        else:
            print('Team 2\'s lead of ',team2_points-team1_points,' is not safe')
else:
    print(team1_points,' and ',team2_points,' are equal - no one is in the lead')

        
