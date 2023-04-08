def initialize_n_and_colored_paper():
    global n,color_paper
    n = int(input())
    color_paper = [list(map(int, input().split())) for _ in range(n)]


def get_from_divided_paper(x,y,n):
    color = color_paper[x][y]
    
    for i in range(x,x+n):
        for j in range(y, y+ n):
            if color != color_paper[i][j]:
                return 3
    return color
        
            

def get_the_number_of_white_confetti_and_blue_confetti(x,y,n):
    global white,blue
    square_color  = get_from_divided_paper(x,y,n)
    
    if square_color == 0 : white +=1 
    
    elif square_color == 1: blue +=1 
        
    else : 
        get_the_number_of_white_confetti_and_blue_confetti(x, y, n // 2)                   # 1사분면
        get_the_number_of_white_confetti_and_blue_confetti(x, y + n // 2, n // 2)          # 2사분면
        get_the_number_of_white_confetti_and_blue_confetti(x + n // 2, y, n // 2)          # 3사분면
        get_the_number_of_white_confetti_and_blue_confetti(x + n // 2, y + n // 2, n // 2) # 4사분면
    
    
n = 0
color_paper = []
initialize_n_and_colored_paper()


white = 0
blue = 0
get_the_number_of_white_confetti_and_blue_confetti(0,0,n)
print(white)
print(blue)



#문제 해석 : 종이를 4등분하여 분할된 정사각형 구역의 색종이가 모두 같은 색이라면 하나의 색종이로써 인식한다.
#           인식된 색종이는 흰색과 파란색으로 구분되며 각 색종이의 개수를 구하여라 


#문제 접근 : 종이를 4등분하여(divide)하여 접근 가능하다면(conquer) 색종이로 보고 아니라면 해당 구역을 다시 4등분하여 접근한다.
#           등분과 접근 가능이 깊이있게 반복한다. -> 재귀
#           재귀를 사용해서 등분하게되며, Base Case 로써 접근 가능을 조건을 두어 계산한다. 


#일반적인 분할정복 pseudo code 
#def f(x):
#    if f(x)가 계산가능하다면:
#        return f(x)를 계산한 값 # 정복
#    else:
#        x를 x1, x2로 분할
#        f(x1)과 f(x2) 호출 # 분할
#        return f(x1), f(x2)로 구한 값 # 조합


# 처음에 이렇게 4개로 2차원 리스트를 분할하려 했으나 생각대로 분할되지 않더군요! 그래서 dx,dy를 통해 새롭게 분할하게 되었습니다.     
# find_the_number_of_white_confetti_and_blue_confetti(paper[:len(paper)//2][:len(paper)//2]) #1사분면 
# find_the_number_of_white_confetti_and_blue_confetti(paper[len(paper)//2:][:len(paper)//2]) #2사분면
# find_the_number_of_white_confetti_and_blue_confetti(paper[:len(paper)//2][len(paper)//2:]) #3사분면
# find_the_number_of_white_confetti_and_blue_confetti(paper[len(paper)//2:][len(paper)//2:]) #4사분면