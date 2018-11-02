def player_points ():

    name = input ("What is the name of your player?")

    passing_yards = input ("How many passing yards did your player get?")
    #1 point for every 25 yards
    py_points = int(passing_yards)/25

    passing_touchdowns = input ("How many passing touchdowns did your player get?")
    #4 points for every passing touchdown
    pt_points = int(passing_touchdowns) * 4

    interceptions = input ("How many interceptions did your player get?")
    #-2 points for every interception
    i_points = int (interceptions) * -2

    rushing_yards = input ("How many rushing yards did your player get?")
    #1 point for every 10 rushing yards
    ry_points = int (rushing_yards)/10

    rushing_touchdowns = input ("How many rushing touchdowns did your player get?")
    #6 points for every ruching touchdown
    rt_points = int(rushing_touchdowns) * 6

    recieving_yards = input ("How many recieving yards did your player get?")
    #1 point for every 10 yards
    rey_points = int (recieving_yards)/10

    recieving_touchdowns = input ("How many recieving touchdowns did your player get?")
    #6 points for every reciveing touchdown
    ret_points = int(recieving_touchdowns)*6

    fumble_recovered = input ("How many times did your player recover a fumbled touchdown?")
    #6 points for every fumbled recoverd for a touchdown
    fr_points = int(fumble_recovered)*6

    two_point_conversion = input ("How many 2 point conversions did your player get?")
    #2 points for every 2 point conversion
    tpc_points = int(two_point_conversion) * 2

    fumbles_lost = input ("How many fumbles lost did your player get?")
    #-2 points for every fumble
    fl_points = int(fumbles_lost)*-2

    total_points = str(py_points + pt_points + i_points +ry_points + rt_points + rey_points+ ret_points + fr_points + tpc_points+fl_points)

    print(name + " scored a toal of " + total_points + " points")

def call_for_all_players():
    while True:
        question = input ("Would you like to calculate the score for another player? (Y/N)")
        if question == "Y":
            player_points()

call_for_all_players() 
