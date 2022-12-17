import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

//정답 참고
//https://codevang.tistory.com/316

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int curTime = 0;
        int jobsIdx = 0;
        int completeCount = 0;

        Arrays.sort(jobs, Comparator.comparingInt(a -> a[0]));

        PriorityQueue<int[]> waitingQueue = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));

        while (completeCount < jobs.length) {
            while (jobsIdx < jobs.length && jobs[jobsIdx][0] <= curTime) {
                waitingQueue.add(jobs[jobsIdx]);
                jobsIdx++;
            }

            if (waitingQueue.isEmpty()) {
                curTime = jobs[jobsIdx][0];
            } else {
                int[] job = waitingQueue.poll();
                answer += curTime + job[1] - job[0];
                curTime += job[1];
                completeCount++;
            }
        }

        return answer / jobs.length;
    }
}
