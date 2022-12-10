import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static public void main(String[] args) throws IOException {
        Solution ts = new Solution();

//      *BufferedReader*
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstInput = br.readLine().split(" ");
        int counselCount = Integer.parseInt(firstInput[0]);

        List<Counsel> counsels = new ArrayList<>();
        counsels.add(new Counsel("0", "0"));
        for (int i = 0; i < counselCount; i++) {
            String[] tempSplits = br.readLine().split(" ");

            counsels.add(new Counsel(tempSplits[0], tempSplits[1]));
        }
        counsels.add(new Counsel("0", "0"));

        System.out.println(ts.solution(counselCount, counsels));
    }
}

class Counsel {
    int time;
    int price;

    public Counsel(String time, String price) {
        this.time = Integer.parseInt(time);
        this.price = Integer.parseInt(price);
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

