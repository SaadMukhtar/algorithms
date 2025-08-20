class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        newImg = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                found = 0
                sum = 0
                for i in [0, 1, -1]:
                    for k in [0, 1, -1]:
                        if 0 <= r+i < ROWS and 0 <= c+k < COLS:
                            found += 1
                            sum += img[r+i][c+k]
                newImg[r][c] = sum // found if found else 0
        return newImg
