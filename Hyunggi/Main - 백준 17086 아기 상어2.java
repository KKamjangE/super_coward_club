import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static public void main(String[] args) throws IOException {
        Solution ts = new Solution();

        // *BufferedReader*
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] variable = br.readLine().split(" ");
        int row = Integer.parseInt(variable[0]);
        int col = Integer.parseInt(variable[1]);

        int[][] matrix = new int[row][col];

        for (int r = 0; r < row; r++) {
            String[] tempLine = br.readLine().split(" ");
            for (int c = 0; c < tempLine.length; c++) {
                matrix[r][c] = Integer.parseInt(tempLine[c]);
            }
        }

        System.out.println(ts.solution(row, col, matrix));
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

