import random
import time
import os

# 定数
CHOICES = ['グー', 'チョキ', 'パー']
WINNING_SCORE = 5

# 対応表（勝敗）
WIN_RULES = {
    'グー': 'チョキ',
    'チョキ': 'パー',
    'パー': 'グー'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_intro():
    clear_screen()
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("　🎮 じゃんけんバトル：決戦編 🎮")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("最初に5回勝った方が勝者だ！")
    print("君は勝てるかな？")
    input("\nEnterキーでスタート！")

def get_player_choice():
    print("\nあなたの手を選んでください：")
    for idx, choice in enumerate(CHOICES, 1):
        print(f"{idx}. {choice}")
    while True:
        try:
            selection = int(input("番号を入力 (1-3): "))
            if 1 <= selection <= 3:
                return CHOICES[selection - 1]
        except ValueError:
            pass
        print("無効な入力です。もう一度！")

def get_cpu_choice(player_history):
    # CPUはランダムだが、プレイヤーの過去の手を少し考慮
    if not player_history:
        return random.choice(CHOICES)
    most_common = max(set(player_history), key=player_history.count)
    # プレイヤーがよく出す手に勝てる手を出す確率を上げる
    counter_hand = None
    for k, v in WIN_RULES.items():
        if v == most_common:
            counter_hand = k
            break
    weights = [0.2, 0.2, 0.2]
    for i, c in enumerate(CHOICES):
        if c == counter_hand:
            weights[i] = 0.6
    return random.choices(CHOICES, weights=weights)[0]

def print_janken_animation():
    print("\nじゃんけん...")
    time.sleep(0.5)
    print("ぽん！")
    time.sleep(0.3)

def determine_winner(player, cpu):
    if player == cpu:
        return 'draw'
    elif WIN_RULES[player] == cpu:
        return 'player'
    else:
        return 'cpu'

def print_round_result(player, cpu, winner):
    print(f"\nあなた：{player}")
    print(f"コンピュータ：{cpu}")
    if winner == 'draw':
        print("→ あいこでしょ！")
    elif winner == 'player':
        print("→ あなたの勝ち！🎉")
    else:
        print("→ コンピュータの勝ち！💻")

def play_game():
    player_score = 0
    cpu_score = 0
    round_num = 1
    player_history = []

    while player_score < WINNING_SCORE and cpu_score < WINNING_SCORE:
        print(f"\n=== 第{round_num}ラウンド ===")
        player_choice = get_player_choice()
        cpu_choice = get_cpu_choice(player_history)
        player_history.append(player_choice)

        print_janken_animation()

        winner = determine_winner(player_choice, cpu_choice)
        print_round_result(player_choice, cpu_choice, winner)

        if winner == 'player':
            player_score += 1
        elif winner == 'cpu':
            cpu_score += 1

        print(f"\nスコア： あなた {player_score} - コンピュータ {cpu_score}")
        round_num += 1
        time.sleep(1)

    print("\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    if player_score > cpu_score:
        print("🎉🎉 あなたの勝利！！ 🎉🎉")
    else:
        print("💻 コンピュータの勝利！また挑戦してね 💻")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")

def ask_replay():
    while True:
        again = input("\nもう一度遊びますか？ (y/n): ").lower()
        if again in ['y', 'n']:
            return again == 'y'
        print("y か n を入力してください。")

def main():
    while True:
        print_intro()
        play_game()
        if not ask_replay():
            print("\n👋 遊んでくれてありがとう！またね！")
            break

if __name__ == "__main__":
    main()
