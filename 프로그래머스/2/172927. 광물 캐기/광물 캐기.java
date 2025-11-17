import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        int totalPicks = picks[0] + picks[1] + picks[2];
        // 곡괭이로 캘 수 있는 최대 광물 개수
        int maxMinerals = Math.min(totalPicks * 5, minerals.length);

        // 5개씩 자른 그룹: [다이아 개수, 철 개수, 돌 개수]
        List<int[]> groups = new ArrayList<>();

        for (int i = 0; i < maxMinerals; i++) {
            int groupIdx = i / 5;
            if (groups.size() <= groupIdx) {
                groups.add(new int[3]); // 0: dia, 1: iron, 2: stone
            }

            String m = minerals[i];
            int[] group = groups.get(groupIdx);

            if (m.equals("diamond")) {
                group[0]++;
            } else if (m.equals("iron")) {
                group[1]++;
            } else { // "stone"
                group[2]++;
            }
        }

        // 그룹을 "돌 곡괭이로 캤을 때 피로도" 기준으로 내림차순 정렬
        // 돌 곡괭이 피로도: dia=25, iron=5, stone=1
        groups.sort((a, b) -> {
            int fatigueA = a[0] * 25 + a[1] * 5 + a[2];
            int fatigueB = b[0] * 25 + b[1] * 5 + b[2];
            return fatigueB - fatigueA; // 내림차순
        });

        int answer = 0;
        int idx = 0; // groups 인덱스

        // 정렬된 그룹에 곡괭이를 순서대로 배치
        for (int[] group : groups) {
            int pickType = -1; // 0: dia, 1: iron, 2: stone

            if (picks[0] > 0) {
                pickType = 0;
                picks[0]--;
            } else if (picks[1] > 0) {
                pickType = 1;
                picks[1]--;
            } else if (picks[2] > 0) {
                pickType = 2;
                picks[2]--;
            } else {
                // 더 이상 사용할 곡괭이가 없으면 종료
                break;
            }

            int diaCnt = group[0];
            int ironCnt = group[1];
            int stoneCnt = group[2];

            if (pickType == 0) {
                // 다이아 곡괭이: 모든 광물 피로도 1
                answer += diaCnt * 1 + ironCnt * 1 + stoneCnt * 1;
            } else if (pickType == 1) {
                // 철 곡괭이: dia=5, iron=1, stone=1
                answer += diaCnt * 5 + ironCnt * 1 + stoneCnt * 1;
            } else {
                // 돌 곡괭이: dia=25, iron=5, stone=1
                answer += diaCnt * 25 + ironCnt * 5 + stoneCnt * 1;
            }

            idx++;
        }

        return answer;
    }
}
