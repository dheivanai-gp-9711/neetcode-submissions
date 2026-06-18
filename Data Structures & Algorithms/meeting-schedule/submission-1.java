/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {

        if(intervals.size() <=1)
        {
            return true;
        }
        Collections.sort(intervals, Comparator.comparingInt(i->i.end));
        int freeTime = intervals.get(0).end;
        int count=1;
        for(int i =1;i<intervals.size();i++)
        {
            if(intervals.get(i).start >= freeTime)
            {
                freeTime = intervals.get(i).end;
                count+=1;
            }
        }
        return intervals.size() == count;
    }
}
