class Solution {
    final int EMPTY = 0;
    final int WALL = 1;
    final int VIRUS = 2;

    int result;
    int[][] temp;
    int[][] gTables;

    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private int gRow;
    private int gCol;

    public int solution(int row, int col, int[][] tables) {
        temp = new int[row][col];
        gRow = row;
        gCol = col;
        gTables = tables;

        dfs(0);

        return result;
    }

    private void dfs(int count) {
        if (count == 3) {
            tableDeepCopy();

            runAllVirus();

            result = Math.max(result, getMaxScore());

            return;
        }

        for (int r = 0; r < gTables.length; r++) {
            for (int c = 0; c < gTables[r].length; c++) {
                if (gTables[r][c] == EMPTY) {
                    gTables[r][c] = WALL;
                    dfs(count + 1);
                    gTables[r][c] = EMPTY;
                }
            }
        }
    }

    private int getMaxScore() {
        int maxScore = 0;

        for (int[] rows : temp) {
            for (int col : rows) {
                if (col == EMPTY) {
                    maxScore++;
                }
            }
        }

        return maxScore;
    }

    private void runAllVirus() {
        for (int r = 0; r < temp.length; r++) {
            for (int c = 0; c < temp[r].length; c++) {
                if (temp[r][c] == VIRUS) {
                    runVirus(r, c);
                }
            }
        }
    }

    private void tableDeepCopy() {
        for (int i = 0; i < gTables.length; i++) {
            System.arraycopy(gTables[i], 0, temp[i], 0, gTables[i].length);
        }
    }

    private boolean isOutOfTable(int e_r, int e_c) {
        return e_r < 0 || e_c < 0 || e_r >= gRow || e_c >= gCol;
    }

    private void runVirus(int r, int c) {
        for (int[] dir : directions) {
            int e_r = r + dir[0];
            int e_c = c + dir[1];

            if (isOutOfTable(e_r, e_c)) {
                continue;
            }

            if (temp[e_r][e_c] == EMPTY) {
                temp[e_r][e_c] = VIRUS;
                runVirus(e_r, e_c);
            }
        }
    }

}
