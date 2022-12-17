import java.io.IOException;


public class Main {
    static public void main(String[] args) throws IOException {
        Solution ts = new Solution();

        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
//        int[][] jobs = {{0, 1}, {1, 1}, {50, 7}};

        System.out.println(ts.solution(jobs));
    }
}

//public class Main{
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int cordiNum = Integer.parseInt(br.readLine());
//
//        StringTokenizer st;
//
//        List<Coordinate> coordinateList = new ArrayList<Coordinate>();
//
//        for(int i = 0; i<cordiNum; i++){
//            st = new StringTokenizer(br.readLine());
//            int x = Integer.parseInt(st.nextToken());
//            int y = Integer.parseInt(st.nextToken());
//            coordinateList.add(new Coordinate(x, y));
//        }
//    }
//}

//안쓰는 코드 모음

//        *Sacnner*
//        Scanner scanner = new Scanner(System.in);
//        String testCaseNumStr = scanner.nextLine();
//        int testCaseNum = Integer.parseInt(testCaseNumStr);
//        String[] testCaseArray = new String[testCaseNum];
//
//        for (int i = 0; i < testCaseNum; i++) {
//            testCaseArray[i] = scanner.nextLine();
//        }

//        *StringTokenizer*
//        StringTokenizer st;
//        st = new StringTokenizer(br.readLine());
//        int stNum = Integer.parseInt(st.nextToken());
//        int testValue = Integer.parseInt(br.readLine());

//        *BufferedReader*
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        int testCaseNum = Integer.parseInt(br.readLine());
//        String[] testCase = new String[testCaseNum];
//        for (int i = 0; i < testCaseNum; i++) {
//            testCase[i] = br.readLine();
//        }

//    // N의 진짜 약수의 개수
//    int testCase = Integer.parseInt(br.readLine());
//    int[] inputArray = new int[testCase];
//
//    // N의 진짜 약수
//    StringTokenizer st;
//        st = new StringTokenizer(br.readLine());
//                for (int i = 0; i < testCase; i++) {
//        inputArray[i] = Integer.parseInt(st.nextToken());
//        }

