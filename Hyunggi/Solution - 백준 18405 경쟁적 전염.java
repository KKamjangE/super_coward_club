import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    final int EMPTY = 0;

    int[][] gTables;

    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private int gRowCol;

    public int solution(int rowCol, int virusCount, int[][] tables, int[] condition) {
        gRowCol = rowCol;
        gTables = tables;

        int timeLimit = condition[0];
        int targetRow = condition[1];
        int targetCol = condition[2];

        PriorityQueue<Virus> pq = new PriorityQueue<>();
        Queue<Virus> waitingQue = new LinkedList<>();

        for (int r = 0; r < gRowCol; r++) {
            for (int c = 0; c < gRowCol; c++) {
                if (tables[r][c] != EMPTY) {
                    pq.offer(new Virus(tables[r][c], r, c));
                }
            }
        }

        int curTime = 0;

        while (!pq.isEmpty()) {
            if (curTime == timeLimit) {
                break;
            }

            Virus virus = pq.poll();

            int curRow = virus.row;
            int curCol = virus.col;

            for (int[] direction : directions) {
                int editRow = curRow + direction[0];
                int editCol = curCol + direction[1];

                if (isOutOfTable(editRow, editCol)) {
                    continue;
                }

                if (tables[editRow][editCol] == EMPTY) {
                    tables[editRow][editCol] = virus.priority;
                    waitingQue.offer(new Virus(virus.priority, editRow, editCol));
                }
            }

            if (pq.isEmpty()) {
                curTime += 1;
                while (!waitingQue.isEmpty()) {
                    Virus tempVirus = waitingQue.poll();
                    pq.offer(tempVirus);
                }
            }
        }

        return tables[targetRow - 1][targetCol - 1];
    }

    boolean isOutOfTable(int row, int col) {
        return row < 0 || col < 0 || row >= gRowCol || col >= gRowCol;
    }
}

class Virus implements Comparable<Virus> {
    int priority;
    int row;
    int col;

    public Virus(int priority, int row, int col) {
        this.priority = priority;
        this.row = row;
        this.col = col;
    }

    @Override
    public int compareTo(Virus o) {
        return Integer.compare(this.priority, o.priority);
    }
}
