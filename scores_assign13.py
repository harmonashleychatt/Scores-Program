# starting the try block
try:
    outfile = open('grades.txt', 'r')
# opening the file in read mode
    rows = 0
    maxscore = 0
    studentmaxscore = ' '
# assigning varibles to count
    for item in outfile:
# for loop for the file
        rows += 1
# adding each field in the file
        item_list = item.split(';')
# separating fields
        score = item_list[1]
        Score = int(score)
        if Score >= maxscore:
            maxscore = int(item_list[1])
            studentmaxscore = item_list[0]
    print("Highest Score:", studentmaxscore,",",maxscore)
    print("Number of records:", rows)
# displaying results
except IOError:
    print('An error occurred trying to read this file.')
except:
    print('An unknown error occurred.')
finally:
    print('End.')