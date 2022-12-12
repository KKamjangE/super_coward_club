//정답 코드 참조
//https://zoosso.tistory.com/414

class Solution {
    final int[] team1 = {0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4};
    final int[] team2 = {1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5};
    final int WIN = 0;
    final int DRAW = 1;
    final int LOSE = 2;
    int[] answer = new int[4];
    int[][] match = new int[6][3];
    int[][] result = new int[6][3];

    public void solution(int[][] tables) {
        for (int tc = 0; tc < tables.length; tc++) {
            for (int r = 0; r < 6; r++) {
                for (int c = 0; c < 3; c++) {
                    match[r][c] = tables[tc][(3 * r) + c];
                }
            }

            dfs(tc, 0);
        }

        String[] answerString = new String[4];

        for (int i = 0; i < answer.length; i++) {
            answerString[i] = String.valueOf(answer[i]);
        }

        System.out.println(String.join(" ", answerString));
    }

    private void dfs(int tc, int round) {
        // 15개 경기 종료
        if (round == 15) {
            //이미 가능한 경우로 판단되는 경우
            if (answer[tc] == 1) {
                return;
            }

            for (int r = 0; r < 6; r++) {
                for (int c = 0; c < 3; c++) {
                    //한 곳이라도 맞지 않는 경우에는 false
                    if (match[r][c] != result[r][c]) {
                        return;
                    }
                }
            }

            answer[tc] = 1;
            return;
        }

        // 승리 0, 무승부 1, 패배 2
        int t1 = team1[round];
        int t2 = team2[round];

        // t1 승, t2 패
        result[t1][WIN]++;
        result[t2][LOSE]++;
        dfs(tc, round + 1);
        result[t1][WIN]--;
        result[t2][LOSE]--;
        // t1 무, t2 무
        result[t1][DRAW]++;
        result[t2][DRAW]++;
        dfs(tc, round + 1);
        result[t1][DRAW]--;
        result[t2][DRAW]--;
        // t1 패, t2 승
        result[t1][LOSE]++;
        result[t2][WIN]++;
        dfs(tc, round + 1);
        result[t1][LOSE]--;
        result[t2][WIN]--;
    }
}
