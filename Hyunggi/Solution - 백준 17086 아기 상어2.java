import java.util.LinkedList;
import java.util.Queue;

class Solution {
    int answer;
    int gRow;
    int gCol;
    int[][] gMatrix;

    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

    public int solution(int row, int col, int[][] matrix) {
        answer = 0;
        gMatrix = matrix;
        gRow = row;
        gCol = col;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                bfs(r, c);
            }
        }

        return answer;
    }

    void bfs(int row, int col) {
        boolean[][] visited = new boolean[gRow][gCol];

        Queue<Coordi> queue = new LinkedList<>();

        visited[row][col] = true;
        queue.add(new Coordi(row, col, 0));

        while (!queue.isEmpty()) {
            Coordi cur = queue.poll();

            if (gMatrix[cur.r][cur.c] == 1) {
                answer = Math.max(answer, cur.dis);
                return;
            }

            for (int[] dir : directions) {
                int eR = cur.r + dir[0];
                int eC = cur.c + dir[1];
                int eD = cur.dis + 1;

                if (isOutOfMatrix(eR, eC)) {
                    continue;
                }

                if (!visited[eR][eC]) {
                    visited[eR][eC] = true;
                    queue.add(new Coordi(eR, eC, eD));
                }
            }
        }

    }

    boolean isOutOfMatrix(int r, int c) {
        return r < 0 || r >= gRow || c < 0 || c >= gCol;
    }
}

class Coordi {
    int r;
    int c;
    int dis;

    public Coordi(int r, int c, int dis) {
        this.r = r;
        this.c = c;
        this.dis = dis;
    }
}
