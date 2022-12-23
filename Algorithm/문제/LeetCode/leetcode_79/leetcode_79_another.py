class Solution(object):
    def exist(self, board, word):
        global answer_flag, move
        # 단어 길이 1인 경우 예외처리
        if len(word) == 1:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word:
                        return True
            return False

        # 알파벳이 이미 부족한 경우 return False
        alpa_list = set(list(word))
        check_list = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                check_list.append(board[i][j])

        for i in alpa_list:
            if i not in check_list:
                return False

            # 첫 번째와 두 번째 글자 기준으로 첫 번째 글자 위치들 찾기
        answer_flag = False
        first_alpa = word[0]
        second_alpa = word[1]
        first_alpa_list = []

        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_alpa:
                    for k in range(len(move)):
                        x = i + move[k][0]
                        y = j + move[k][1]
                        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][
                            y] == second_alpa and [i, j] not in first_alpa_list:
                            first_alpa_list.append([i, j])

                        # 단어 찾는 함수

        def find_word(i, j, cnt, word, visited):
            global answer_flag, move
            if cnt == len(word):
                answer_flag = True
                return
            else:
                visited = list(visited)
                visited.append([i, j])
                find_alpa = word[cnt]
                for k in range(len(move)):
                    x = i + move[k][0]
                    y = j + move[k][1]
                    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == find_alpa and [x,
                                                                                                                    y] not in visited:
                        find_word(x, y, cnt + 1, word, visited)

        # 첫 번째 글자들 하나하나 돌려보기
        for i in range(len(first_alpa_list)):
            visited = [[first_alpa_list[i][0], first_alpa_list[i][1]]]
            find_word(first_alpa_list[i][0], first_alpa_list[i][1], 1, word, visited)
            if answer_flag == True:
                return True

        return False