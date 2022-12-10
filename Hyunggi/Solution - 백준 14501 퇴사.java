import java.util.List;

// 정답 참고
// https://velog.io/@hammii/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-java

class Solution {
    public int solution(int counselCount, List<Counsel> counsels) {

        // 구현한 방식의 DP 배열은 그 날짜부터 시작했을 때의 최댓값

        // 즉, DP[4]는 4일부터 N일까지 최댓값
        // 우리가 원하는 것은 1일부터이므로 DP[1]의 값을 구해주면 된다.

        // 뒤에서부터 생각하는 게 더 쉽다.

        // 일할 수 있는 날짜를 넘어가는 경우: 어차피 일을 하지 못하므로 바로 다음 dp 값으로 설정해 준다.
        // 일할 수 있는 날짜인 경우: 일하지 않았을 때(dp[i+1])와 일했을 때 총 벌 수 있는 금액(dp[next]+P[i])을 비교해 준다.

        int[] dp = new int[counselCount + 2]; // 0 과 마지막 날에 + 1 를 고려

        for (int curDay = counselCount; curDay >= 1; curDay--) {
            Counsel curCounsel = counsels.get(curDay);
            int nextDay = curDay + curCounsel.time;

            if (nextDay > counselCount + 1) {
                dp[curDay] = dp[curDay + 1];
            } else {
                dp[curDay] = Math.max(dp[curDay + 1], dp[nextDay] + curCounsel.price);
            }
        }

        return dp[1];
    }
}
