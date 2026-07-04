impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::<(usize, i32)>::new(); n + 1];

        for road in roads {
            let u = road[0] as usize;
            let v = road[1] as usize;
            let d = road[2];
            graph[u].push((v, d));
            graph[v].push((u, d));
        }

        let mut visited = vec![false; n + 1];
        let mut stack = vec![1usize];
        visited[1] = true;
        let mut ans = i32::MAX;

        while let Some(node) = stack.pop() {
            for &(next, dist) in &graph[node] {
                ans = ans.min(dist);
                if !visited[next] {
                    visited[next] = true;
                    stack.push(next);
                }
            }
        }

        ans
    }
}