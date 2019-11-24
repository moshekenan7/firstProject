# This add_score method updates the Scores file
def add_score(points):
    scores_file = open("Scores.txt", 'r+')
    cur_score = scores_file.read()
    #print(cur_score)
    int_score = 0
    if cur_score != "":
        #print(cur_score)
        int_score = int(cur_score)
    new_score = int_score + points
    print("new score is: " + str(new_score))
    scores_file.seek(0)
    scores_file.write(str(new_score))
    scores_file.close()
