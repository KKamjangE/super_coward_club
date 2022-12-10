import java.util.PriorityQueue;

class Solution {
    void initParents(int[] parents) {
        for (int i = 0; i < parents.length; i++) {
            parents[i] = i;
        }
    }

    //unionParent : 두 노드의 부모를 합친다
    void unionParent(int[] parents, int node1, int node2) {
        int node1Parent = getParent(parents, node1);
        int node2Parent = getParent(parents, node2);

        if (node1Parent < node2Parent) {
            parents[node2Parent] = node1Parent;
        } else {
            parents[node1Parent] = node2Parent;
        }
    }

    //findParent : 두 노드의 부모가 같은지 확인
    boolean findParent(int[] parents, int node1, int node2) {
        int node1Parent = getParent(parents, node1);
        int node2Parent = getParent(parents, node2);

        return node1Parent == node2Parent;
    }

    //getParent : 부모의 노드를 찾는다.
    int getParent(int[] parents, int node) {
        if (parents[node] == node) {
            return node;
        }

        int myParent = parents[node];

        return parents[node] = getParent(parents, myParent);
    }

    public long solution(int tableLength, int[][] tables) {
        long answer = 0;

        int[] parents = new int[tableLength];
        initParents(parents);

        PriorityQueue<PlanetCoordinate> x = new PriorityQueue<>();
        PriorityQueue<PlanetCoordinate> y = new PriorityQueue<>();
        PriorityQueue<PlanetCoordinate> z = new PriorityQueue<>();

        PriorityQueue<PlanetDistance> pq = new PriorityQueue<PlanetDistance>();

        for (int i = 0; i < tables.length; i++) {
            x.add(new PlanetCoordinate(tables[i][0], i));
            y.add(new PlanetCoordinate(tables[i][1], i));
            z.add(new PlanetCoordinate(tables[i][2], i));
        }

        PlanetCoordinate saveX = x.poll();
        PlanetCoordinate saveY = y.poll();
        PlanetCoordinate saveZ = z.poll();

        while (!x.isEmpty()) {
            PlanetCoordinate tempX = x.poll();
            PlanetCoordinate tempY = y.poll();
            PlanetCoordinate tempZ = z.poll();

            PlanetDistance pdX = new PlanetDistance((tempX.coordinate - saveX.coordinate), tempX.planetNum, saveX.planetNum);
            PlanetDistance pdY = new PlanetDistance((tempY.coordinate - saveY.coordinate), tempY.planetNum, saveY.planetNum);
            PlanetDistance pdZ = new PlanetDistance((tempZ.coordinate - saveZ.coordinate), tempZ.planetNum, saveZ.planetNum);

            pq.add(pdX);
            pq.add(pdY);
            pq.add(pdZ);

            saveX = tempX;
            saveY = tempY;
            saveZ = tempZ;
        }

        while (!pq.isEmpty()) {
            PlanetDistance planetDistance = pq.poll();
            int planetNum1 = planetDistance.planetNum1;
            int planetNum2 = planetDistance.planetNum2;

            if (!findParent(parents, planetNum1, planetNum2)) {
                unionParent(parents, planetNum1, planetNum2);
                answer += planetDistance.distance;
            }
        }

        return answer;
    }
}

class PlanetCoordinate implements Comparable<PlanetCoordinate> {
    int coordinate;
    int planetNum;

    public PlanetCoordinate(int coordinate, int planetNum) {
        this.coordinate = coordinate;
        this.planetNum = planetNum;
    }

    @Override
    public int compareTo(PlanetCoordinate o) {
        return Integer.compare(this.coordinate, o.coordinate);
    }
}

class PlanetDistance implements Comparable<PlanetDistance> {
    int distance;
    int planetNum1;
    int planetNum2;

    public PlanetDistance(int distance, int planetNum1, int planetNum2) {
        this.distance = distance;
        this.planetNum1 = planetNum1;
        this.planetNum2 = planetNum2;
    }

    @Override
    public int compareTo(PlanetDistance o) {
        return Integer.compare(this.distance, o.distance);
    }
}


