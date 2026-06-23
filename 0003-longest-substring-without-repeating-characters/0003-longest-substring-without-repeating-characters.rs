use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut map = HashMap::new();
        let mut left = 0;
        let mut ans = 0;

        for (right, ch) in s.chars().enumerate() {
            if let Some(&idx) = map.get(&ch) {
                left = left.max(idx + 1);
            }

            map.insert(ch, right);
            ans = ans.max(right - left + 1);
        }

        ans as i32
    }
}