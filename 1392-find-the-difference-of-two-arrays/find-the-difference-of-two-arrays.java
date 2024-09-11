class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> distinct1 = new HashSet<Integer>(Arrays.stream(nums1).boxed().collect(Collectors.toList()));
        Set<Integer> distinct2 = new HashSet<Integer>(Arrays.stream(nums2).boxed().collect(Collectors.toList()));

        Set<Integer> copy = new HashSet<Integer>(distinct1);
        distinct1.removeAll(distinct2);
        distinct2.removeAll(copy);

        return new LinkedList<List<Integer>>(
            List.of(
                new LinkedList<>(distinct1),
                new LinkedList<>(distinct2)
            )
        );
    }
}