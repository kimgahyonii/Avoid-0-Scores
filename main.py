import pygame
import sys
import random

# Pygame 초기화
pygame.init()
# 화면 설정, 프레임 속도 제어를 위해서
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# 시험지 이미 로드
paper_images = [
    pygame.image.load(rf"D:\pythonProject\0점을 피해라\images\scorePaper_img\paper_{i}.jpg")
    for i in range(7)
]
paper_100 = paper_images[6]
PAPER_COUNT = 7

# 화면 크기 설정
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))

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
except pygame.error as e:
    print(f"Error loading character image: {e}")
    pygame.quit()
    sys.exit()

# 캐릭터 초기 위치 설정 (화면의 중앙)
character = character_front
character_x = screen_width // 2 - character_front.get_width() // 2
character_y = screen_height // 2 - character_front.get_height() // 2 + 70
character_speed = 10

collected_papers = []
# 시험지 초기 위치 리스트

papers = [
    {
        "image": random.choice(paper_images),
        "x": random.randint(0, 800 - paper_images[0].get_width()),
        "y": random.randint(-600, -50),
        "speed": random.randint(2,5)
    }
    for _ in range(PAPER_COUNT)
]

# 시험지 받을 수 있는 상태
# can_receive_paper = False

# 득점 변수
score = 0
flash_timer = 0
flash_duration = 10

# 게임 진행 확인
running = True
while running:
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
        can_receive_paper = True
    elif keys[pygame.K_w]:
        character = character_receive_paper
    else:
        character = character_front  # 정면 이미지로 복귀
        # can_receive_paper = False # 시험지 받을 수 없는 상태

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

        # 캐릭터와 paper_7 충돌 확인
        if keys[pygame.K_w] and paper["image"] == paper_100:
            if paper["y"] + paper["image"].get_height() > character_y and paper["y"] < character_y + character.get_height():
                if paper["x"] < character_x + character.get_width() and paper["x"] + paper["image"].get_width() > character_x:
                    score += 100
                    flash_timer = flash_duration # 득점 시 깜빡임
                    papers.remove(paper)

    # 득점 시 깜빡임 효과 적용
    if flash_timer > 0:
        flash_timer -= 1
        if flash_timer % 2 == 0:
            screen.fill((255,255,255)) #하얀색으로 화면 깜빡임
    # 캐릭터 이미지 그리기
    screen.blit(character, (character_x, character_y))

    pygame.display.flip()
    clock.tick(20)


# Pygame 종료
pygame.quit()
sys.exit()
