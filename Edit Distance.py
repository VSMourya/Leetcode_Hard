
def minDistance(word1,word2):

    distance = [[a for a in range(len(word1) + 1)] for b in range(len(word2) + 1)]
    for i in range(1, len(word2) + 1):
        distance[i][0] = distance[i - 1][0] + 1

    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            if word2[i - 1] == word1[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(distance[i - 1][j], distance[i - 1][j - 1], distance[i][j - 1])

    return distance[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1,word2))