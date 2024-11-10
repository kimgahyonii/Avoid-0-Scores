import pygame
import sys
import random
import os

# Pygame 초기화
pygame.init()
# 화면 설정, 프레임 속도 제어를 위해서
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

paper_speed = 5

# def move_paper(paper):


PAPER_COUNT = 7
scores = [0, 30, 50, 70, 80, 90, 100]


# current_directory = os.path.dirname(_)
paper_images = [
    pygame.image.load(rf"D:\pythonProject\0점을 피해라\images\scorePaper_img\page_{i}.png")
    for i in range(PAPER_COUNT)
]

torn_paper_images = [
    pygame.image.load(rf"D:\pythonProject\0점을 피해라\images\tornPapers\tornpage_{i}.png")
    for i in range(PAPER_COUNT)
]


paper_100 = paper_images[6]
# 화면 크기 설정
screen_width, screen_height = 1000, 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 로드
try:
    background = pygame.image.load(r"D:\pythonProject\0점을 피해라\images\background1.jpeg")
    background = pygame.transform.scale(background, (screen_width, screen_height))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    pygame.quit()
    sys.exit()

# 캐릭터 이미지 로드
try:
    character_front = pygame.image.load(r"D:\pythonProject\0점을 피해라\images\character_img\main_character.png")  # 정면 이미지 경로
    character_left = pygame.image.load(r"D:\pythonProject\0점을 피해라\images\character_img\character_left.png")   # 왼쪽 이미지 경로
    character_right = pygame.image.load(r"D:\pythonProject\0점을 피해라\images\character_img\character_right.png") # 오른쪽 이미지 경로
    character_receive_paper = pygame.image.load(r"D:\pythonProject\0점을 피해라\images\character_img\character_catch.png")
    character_front = pygame.transform.scale(character_front, (200, 200))
    character_left = pygame.transform.scale(character_left, (200, 200))
    character_right = pygame.transform.scale(character_right, (200, 200))
    character_receive_paper = pygame.transform.scale(character_receive_paper,(200,200))
    character_height = character_front.get_rect().height
    character_width = character_front.get_rect().width
except pygame.error as e:
    print(f"Error loading character image: {e}")
    pygame.quit()
    sys.exit()

# 시험지 크기 설정
new_width = paper_images[0].get_width() // 2  # 원본 너비의 절반
new_height = paper_images[0].get_height() // 2  # 원본 높이의 절반

# 시험지 크기 조정
paper_images = [
    pygame.transform.scale(image, (new_width, new_height)) for image in paper_images
]
torn_paper_images = [
    pygame.transform.scale(image, (new_width, new_height)) for image in torn_paper_images
]

# 시험지 설정
paper_image = pygame.Surface((50, 50))  # 시험지 크기
paper_y_position = 0  # 시험지 초기 y 위치
paper_x_position = 375  # 시험지 x 위치
speed = 2  # 시험지 내려오는 속도

# 캐릭터 초기 위치 설정 (화면의 중앙)
character = character_front
character_x = screen_width // 2 - character_front.get_width() // 2
character_y = screen_height // 2 - character_front.get_height() // 2 + 70
character_speed = 20

# 시험지 초기 위치 리스트
# papers = [
#     {
#         "image": paper_images[i],
#         "number": i,
#         "score": scores[i],
#         "x": random.randint(0, 800 - paper_images[0].get_width()),
#         "y": random.randint(-600, -50),
#         "speed": random.randint(2,5),
#
#     }
#     for i in range(PAPER_COUNT)
# ]
papers = [
    {"image":paper_images[0], "name":"0점 시험지", "score": 0, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 5},
    {"image":paper_images[1], "name":"30점 시험지", "score": 30, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 4},
    {"image":paper_images[2], "name":"50점 시험지", "score": 50, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 3},
    {"image":paper_images[3], "name":"70점 시험지", "score": 70, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 2},
    {"image":paper_images[4], "name":"80점 시험지", "score": 80, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 3},
    {"image":paper_images[5], "name":"90점 시험지", "score": 90, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 0.5},
    {"image":paper_images[6], "name":"100점 시험지", "score": 100, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 5},
]

torn_papers = [
    {"image":torn_paper_images[0], "name":"0점 시험지", "score": 0, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 5},
    {"image":torn_paper_images[1], "name":"30점 시험지", "score": 30, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 4},
    {"image":torn_paper_images[2], "name":"50점 시험지", "score": 50, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 3},
    {"image":torn_paper_images[3], "name":"70점 시험지", "score": 70, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 2},
    {"image":torn_paper_images[4], "name":"80점 시험지", "score": 80, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 3},
    {"image":torn_paper_images[5], "name":"90점 시험지", "score": 90, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 0.5},
    {"image":torn_paper_images[6], "name":"100점 시험지", "score": 100, "x": random.randint(0, screen_width - new_width), "y": -new_height, "speed": 5},
]

chosen_image = random.choice(paper_images)  # 이미지를 한 번 랜덤 선택
# image_index = papers.index(chosen_image)  # 선택된 이미지의 인덱스를 저장

# 선택된 이미지가 papers 리스트 내의 어느 항목에 속하는지 찾기
image_index = -1  # 기본값으로 -1 설정
for index, paper in enumerate(papers):
    if paper["image"] == chosen_image:
        image_index = index
        break

if image_index != -1:
    print(f"선택된 시험지의 인덱스: {image_index}")
else:
    print("선택된 이미지가 papers 리스트에 없습니다.")


# 선택된 이미지가 papers 리스트 내의 어느 항목에 속하는지 찾기
image_index = -1  # 기본값으로 -1 설정
for index, paper in enumerate(papers):
    if paper["image"] == chosen_image:
        image_index = index
        break

if image_index != -1:
    print(f"선택된 시험지의 인덱스: {image_index}")
else:
    print("선택된 이미지가 papers 리스트에 없습니다.")


# 시험지 받을 수 있는 상태
# can_receive_paper = False

# 득점 변수

flash_timer = 0
flash_duration = 10

# 투명도 조절 중인 시험지 리스트
fading_papers = []

# 게임 진행 확인
running = True
start_time = pygame.time.get_ticks()

paper = {
    "image": chosen_image,  # 선택된 이미지
    "number": image_index,  # 이미지의 인덱스를 number로 설정
    "name": f"{scores[image_index]}점 시험지",  # 점수를 기반으로 이름 설정
    "score": scores[image_index],  # 해당 이미지에 맞는 점수 설정
    "x": random.randint(0, screen_width - chosen_image.get_width()),  # 랜덤 x 위치
    "y": random.randint(-600, -50),  # 랜덤 y 위치
    "speed": random.randint(2, 5)  # 랜덤 속도
}
# 함수 정의
def move_paper(paper):
    paper['y'] += paper['speed']
    if paper['y'] > screen_height:
        paper['y'] = random.randint(-600, -50)
        paper['x'] = random.randint(0, screen_width - paper["image"].get_width())
        paper['speed'] = random.randint(2, 5)

while running:
    score = 0
    elapsed_time = (pygame.time.get_ticks() - start_time ) / 100 # 초단위로 변환
    if elapsed_time > 15:
        speed += 1
    paper_y_position += 5

    # 이벤트 발생 체크
    for event in pygame.event.get():
        # 창 닫기
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
        character = character_left  # 왼쪽 방향 이미지로 변경
    elif keys[pygame.K_RIGHT]:
        character_x += character_speed
        character = character_right  # 오른쪽 방향 이미지로 변경

    elif keys[pygame.K_w]:
        character = character_receive_paper
        character_updated = True
        for paper in papers[:]:
            if paper["image"] == paper_images[6]:
                if (paper["y"] + paper["image"].get_height() > character_y and
                    paper["y"] < character_y + character.get_height() and
                    paper["x"] < character_x + character.get_width() and
                    paper["x"] + paper["image"].get_width() > character_x):

                    if 'score' in paper and 'score_added' not in paper:
                        print(f"{paper['score']}점 추가")
                        paper['score_added'] = True

                    # 시험지 위치 리셋
                    paper["y"] = random.randint(-600, -50)
                    paper["x"] = random.randint(0, screen_width - paper["image"].get_width())
                    paper["speed"] = random.randint(2,5)

                flash_timer = flash_duration
                papers.remove(paper) # 기존 시험지 제거

                new_paper = {
                    "image": chosen_image,  # 선택된 이미지
                    "number": image_index,  # 이미지의 인덱스를 number로 설정
                    "score": 100,  # 해당 이미지에 맞는 점수 설정
                    "x": random.randint(0, screen_width - chosen_image.get_width()),  # 랜덤 x 위치
                    "y": random.randint(-600, -50),  # 랜덤 y 위치
                    "speed": random.randint(2, 5)  # 랜덤 속도
                }
                papers.append(new_paper)
                break

    elif keys[pygame.K_a]:
        nearest_paper = None
        min_distance = float('inf')
        for i, paper in enumerate(papers):
            #캐릭터와 시험지 간 거리 계산
            distance = ((paper["x"] - character_x) ** 2 + (paper["y"] - character_y) ** 2) ** 0.5
            if distance < 100 and distance < min_distance:
                nearest_paper = paper
                min_distance = distance
        # 가장 가까운 시험지가 있을 경우 찢어진 이미지로 변경

        if nearest_paper:
            current_index = paper_images.index(nearest_paper["image"])
            torn_image = torn_paper_images[current_index]

            if 'score' in nearest_paper and 'score_added' not in nearest_paper:
                print(f"{nearest_paper['score']}점 추가!")
                nearest_paper['score_added'] = True  # 점수 추가됨 표시

            fading_papers.append({
                "image": torn_image,
                "x": nearest_paper["x"],
                "y": nearest_paper["y"],
                "name": f"{scores[image_index]}점 시험지",  # 점수를 기반으로 이름 설정
                "score": scores[image_index],  # 해당 이미지에 맞는 점수 설정
                "alpha": 255,
                "hold_timer": 100
            })
            papers.remove(nearest_paper)

            # 새로운 시험지를 추가해 리스트 유지
            new_paper = {
                "image": chosen_image,  # 선택된 이미지
                "number": image_index,  # 이미지의 인덱스를 number로 설정
                "name": f"{scores[image_index]}점 시험지",  # 점수를 기반으로 이름 설정
                "score": scores[image_index],  # 해당 이미지에 맞는 점수 설정
                "x": random.randint(0, screen_width - chosen_image.get_width()),  # 랜덤 x 위치
                "y": random.randint(-600, -50),  # 랜덤 y 위치
                "speed": random.randint(2, 5)  # 랜덤 속도
            }
            papers.append(new_paper)

    else:
        character = character_front  # 정면 이미지로 복귀


    # if current_time >= next_spawn_time:
    #     new_paper = {
    #         "image": random.choice(paper_images),
    #         "number": random.randint
    #     }

    # 시험지 떨어뜨리기
    # 각 시험지마다 점수 추가 여부를 추적하는 변수
    # 각 시험지마다 점수 추가 여부를 추적하는 변수
    # for paper in papers:
    #     paper['y'] += paper['speed']  # paper_speed를 paper['speed']로 수정
    #     if 'score_added' not in paper:  # 처음 점수를 추가할 때만
    #         if paper['y'] + new_height >= character_y and character_x < paper[
    #             'x'] + new_width and character_x + character_width > paper['x']:
    #             # if 'score' in paper:
    #             #     print(f"{paper['score']}점 추가!")
    #             #     paper['score_added'] = True  # 점수 추가됨 표시
    #             # else:
    #             #     print(f"{paper['name']}에는 score 키가 없습니다.")
    #
    #     # 시험지가 바닥에 닿았는지 체크
    #     elif paper['y'] >= screen_height:
    #         if 'score' in paper:
    #             print(f"{paper['score']}점 감점ㅁ")  # 점수 출력
    #         else:
    #             print(f"{paper['name']}에는 score 키가 없습니다.")  # score 키가 없을 때 처리

    # 배경 이미지 그리기
    screen.blit(background, (0, 0))

    for paper in papers:
        screen.blit(paper["image"], (paper["x"], paper["y"]))
        # 속도 만큼 아래로 이동
        paper["y"] += paper["speed"]

        if paper["y"] > screen_height:
            paper["y"] = random.randint(-600, -50)
            paper["x"] = random.randint(0, screen_width - paper["image"].get_width())
            paper["speed"] = random.randint(2,5)
            # 새로운 이미지 선택
            paper["image"] = random.choice(paper_images)

        # # 캐릭터와 paper_7 충돌 확인
        if keys[pygame.K_w] and paper["image"] == paper_100:
            if paper["y"] + paper["image"].get_height() > character_y and paper["y"] < character_y + character.get_height():
                if paper["x"] < character_x + character.get_width() and paper["x"] + paper["image"].get_width() > character_x:
                    # score += 100
                    flash_timer = flash_duration # 득점 시 깜빡임
                    papers.remove(paper)

        if keys[pygame.K_a] and paper["y"] + paper["image"].get_height() > character_y and paper["y"] < character_y + character.get_height():
             # torn_image = torn_paper_images[paper_images.index(paper["image"])]
            if paper["x"] < character_x + character.get_width() and paper["x"] + paper["image"].get_width() > character_x:
                torn_image = torn_paper_images[paper_images.index(paper["image"])]
                fading_papers.append({
                    "image":torn_image,
                    "x": paper["x"],
                    "y":paper["y"],

                    "alpha":255,
                    # 2초정도 유지
                    "hold_timer":40,
                    # 멈추는 설정
                    # "speed": 0
                })
                papers.remove(paper)
                new_paper = {
                    "image": chosen_image,  # 선택된 이미지
                    "number": image_index,  # 이미지의 인덱스를 number로 설정
                    "name": f"{scores[image_index]}점 시험지",  # 점수를 기반으로 이름 설정
                    "score": scores[image_index],  # 해당 이미지에 맞는 점수 설정
                    "x": random.randint(0, screen_width - chosen_image.get_width()),  # 랜덤 x 위치
                    "y": random.randint(-600, -50),  # 랜덤 y 위치
                    "speed": random.randint(2, 5)  # 랜덤 속도
                }
                papers.append(new_paper)

    # 득점 시 깜빡임 효과 적용
    if flash_timer > 0:
        flash_timer -= 1
        if flash_timer % 2 == 0:
            screen.fill((255,255,255)) #하얀색으로 화면 깜빡임

    # 흐려지는 효과 적용
    for fading_paper in fading_papers[:]: # 리스트 복사본을 사용해서 반복
        if fading_paper["hold_timer"] > 0:
            fading_paper["hold_timer"] -= 5 # 멈춘 상태 유지
        else:
            fading_paper["alpha"] -= 5 # 투명도 감소

        if fading_paper["alpha"] <= 0:
            fading_papers.remove(fading_paper)
        else:
            temp_image = fading_paper["image"].copy()
            temp_image.set_alpha(int(fading_paper["alpha"]))
            screen.blit(temp_image, (fading_paper["x"], fading_paper["y"]))

    # 캐릭터 이미지 그리기
    screen.blit(character, (character_x, character_y))

    pygame.display.flip()
    clock.tick(15)


# Pygame 종료
pygame.quit()
sys.exit()
