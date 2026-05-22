def player(prev_play, memory={}):
    # Reset lại khi bắt đầu match mới
    if prev_play == "":
        memory.clear()
        memory["opponent_history"] = []
        memory["my_history"] = []
        memory["round"] = 0

    beats = {
        "R": "P",  # Paper beats Rock
        "P": "S",  # Scissors beats Paper
        "S": "R"   # Rock beats Scissors
    }

    opponent_history = memory["opponent_history"]
    my_history = memory["my_history"]

    if prev_play:
        opponent_history.append(prev_play)

    round_num = len(opponent_history)

    # --------- Hàm mô phỏng các bot ---------

    def predict_quincy_next():
        # Quincy pattern thực tế thường là: R, P, P, S, R lặp lại
        pattern = ["R", "P", "P", "S", "R"]
        return pattern[round_num % len(pattern)]

    def predict_kris_next():
        # Kris sẽ chơi nước thắng nước trước đó của mình
        if not my_history:
            return "P"
        return beats[my_history[-1]]

    def predict_mrugesh_next():
        # Mrugesh counter nước xuất hiện nhiều nhất trong 10 nước gần nhất của mình
        last_ten = my_history[-10:]
        if not last_ten:
            most_frequent = "S"
        else:
            most_frequent = max(set(last_ten), key=last_ten.count)
        return beats[most_frequent]

    def abbey_outputs_until_now(my_hist):
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

        abbey_opponent_history = []
        outputs = []

        for i in range(len(my_hist)):
            prev_my_play = "R" if i == 0 else my_hist[i - 1]

            abbey_opponent_history.append(prev_my_play)
            last_two = "".join(abbey_opponent_history[-2:])

            if len(last_two) == 2:
                play_order[last_two] += 1

            potential_plays = [
                prev_my_play + "R",
                prev_my_play + "P",
                prev_my_play + "S"
            ]

            sub_order = {
                k: play_order[k]
                for k in potential_plays
                if k in play_order
            }

            prediction = max(sub_order, key=sub_order.get)[-1]
            outputs.append(beats[prediction])

        return outputs

    def predict_abbey_next():
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

        abbey_opponent_history = []

        # Replay lại lịch sử để tính play_order của Abbey
        for i in range(len(my_history)):
            prev_my_play = "R" if i == 0 else my_history[i - 1]

            abbey_opponent_history.append(prev_my_play)
            last_two = "".join(abbey_opponent_history[-2:])

            if len(last_two) == 2:
                play_order[last_two] += 1

        # Dự đoán lượt tiếp theo
        prev_my_play = my_history[-1] if my_history else "R"

        abbey_opponent_history.append(prev_my_play)
        last_two = "".join(abbey_opponent_history[-2:])

        if len(last_two) == 2:
            play_order[last_two] += 1

        potential_plays = [
            prev_my_play + "R",
            prev_my_play + "P",
            prev_my_play + "S"
        ]

        sub_order = {
            k: play_order[k]
            for k in potential_plays
            if k in play_order
        }

        prediction = max(sub_order, key=sub_order.get)[-1]
        return beats[prediction]

    # --------- Nhận diện bot đang đấu ---------

    def score_quincy():
        pattern = ["R", "P", "P", "S", "R"]
        score = 0
        for i, play in enumerate(opponent_history):
            if play == pattern[i % len(pattern)]:
                score += 1
        return score

    def score_kris():
        score = 0
        for i in range(1, len(opponent_history)):
            predicted = beats[my_history[i - 1]]
            if opponent_history[i] == predicted:
                score += 1
        return score

    def score_mrugesh():
        score = 0
        for i in range(len(opponent_history)):
            previous_my_plays = my_history[:i]
            last_ten = previous_my_plays[-10:]

            if not last_ten:
                most_frequent = "S"
            else:
                most_frequent = max(set(last_ten), key=last_ten.count)

            predicted = beats[most_frequent]

            if opponent_history[i] == predicted:
                score += 1

        return score

    def score_abbey():
        predicted_outputs = abbey_outputs_until_now(my_history)
        score = 0

        for real, predicted in zip(opponent_history, predicted_outputs):
            if real == predicted:
                score += 1

        return score

    # Mấy lượt đầu chơi an toàn để lấy dữ liệu nhận diện bot
    if round_num < 8:
        starter = ["R", "P", "S", "R", "P", "S", "R", "P"]
        move = starter[len(my_history) % len(starter)]
        my_history.append(move)
        return move

    scores = {
        "quincy": score_quincy(),
        "kris": score_kris(),
        "mrugesh": score_mrugesh(),
        "abbey": score_abbey(),
    }

    detected_bot = max(scores, key=scores.get)

    # --------- Chọn chiến thuật counter ---------

    if detected_bot == "quincy":
        predicted_opponent_move = predict_quincy_next()

    elif detected_bot == "kris":
        predicted_opponent_move = predict_kris_next()

    elif detected_bot == "mrugesh":
        predicted_opponent_move = predict_mrugesh_next()

    elif detected_bot == "abbey":
        predicted_opponent_move = predict_abbey_next()

    else:
        predicted_opponent_move = "R"

    # Chơi nước thắng nước dự đoán của đối thủ
    move = beats[predicted_opponent_move]

    my_history.append(move)
    return move