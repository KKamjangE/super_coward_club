import java.util.ArrayList;
import java.util.List;

class Solution {
    // r, c  => 1,1 시작
    // 치킨 거리 = 집과 가장 가까운 치킨집 사이
    // 집을 기준으로 정해짐
    // 도시의 치킨 거리는 모든 집의 치킨 거리의 합
    // 거리는 절대값 으로 계산

    final String EMPTY = "0";
    final String HOUSE = "1";
    final String CHICK = "2";

    public int solution(int tableSize, int restaurantNumber, String[][] tables) {
        List<House> houses = new ArrayList<>();
        List<Chick> chicks = new ArrayList<>();
        int chickNum = 0;
        int houseNum = 0;

        int idx = 0;

        for (int r = 0; r < tableSize; r++) {
            for (int c = 0; c < tableSize; c++) {
                if (tables[r][c].equals(EMPTY)) {
                    continue;
                }

                if (tables[r][c].equals(HOUSE)) {
                    houses.add(new House(r, c));
                    houseNum++;
                } else if (tables[r][c].equals(CHICK)) {
                    chicks.add(new Chick(r, c, idx));
                    idx++;
                    chickNum++;
                }
            }
        }

        int[][] chickDistances = new int[chickNum][houseNum];

        int rIdx = 0;
        for (Chick chick : chicks) {
            int totalDistance = 0;
            int cIdx = 0;
            for (House house : houses) {
                int tempDistance = calculateDistance(chick, house);
                chickDistances[rIdx][cIdx] = tempDistance;
                totalDistance += tempDistance;
                cIdx++;
            }
            chick.sumChickDistance = totalDistance;
            rIdx++;
        }

        chicks.sort(null);

        int rtVal = 0;

        for (int j = 0; j < houseNum; j++) {
            int minValue = (chickDistances[chicks.get(0).idx][j]);
            for (int i = 1; i < restaurantNumber; i++) {
                minValue = Math.min(minValue, (chickDistances[chicks.get(i).idx][j]));
            }
            rtVal += minValue;
        }

        return rtVal;
    }

    int calculateDistance(Chick chick, House house) {
        return Math.abs(chick.r - house.r) + Math.abs(chick.c - house.c);
    }
}

class House {
    int r;
    int c;

    public House(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Chick implements Comparable<Chick> {
    int r;
    int c;
    int idx;

    int sumChickDistance;

    public Chick(int r, int c, int idx) {
        this.r = r;
        this.c = c;
        this.idx = idx;
        sumChickDistance = 0;
    }

    @Override
    public int compareTo(Chick o) {
        return Integer.compare(this.sumChickDistance, o.sumChickDistance);
    }
}
