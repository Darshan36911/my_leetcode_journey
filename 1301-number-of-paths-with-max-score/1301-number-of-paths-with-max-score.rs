impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;

        let n = board.len();
        let board: Vec<Vec<char>> = board.into_iter().map(|s| s.chars().collect()).collect();

        let mut score = vec![vec![-1; n]; n];
        let mut ways = vec![vec![0i64; n]; n];

        score[n - 1][n - 1] = 0;
        ways[n - 1][n - 1] = 1;

        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if board[i][j] == 'X' || (i == n - 1 && j == n - 1) {
                    continue;
                }

                let dirs = [(1, 0), (0, 1), (1, 1)];

                let mut best = -1;
                let mut cnt = 0i64;

                for &(dx, dy) in &dirs {
                    let ni = i + dx;
                    let nj = j + dy;

                    if ni >= n || nj >= n {
                        continue;
                    }

                    if score[ni][nj] == -1 {
                        continue;
                    }

                    if score[ni][nj] > best {
                        best = score[ni][nj];
                        cnt = ways[ni][nj];
                    } else if score[ni][nj] == best {
                        cnt = (cnt + ways[ni][nj]) % MOD;
                    }
                }

                if best == -1 {
                    continue;
                }

                let val = match board[i][j] {
                    'E' | 'S' => 0,
                    c => c.to_digit(10).unwrap() as i32,
                };

                score[i][j] = best + val;
                ways[i][j] = cnt;
            }
        }

        if ways[0][0] == 0 {
            vec![0, 0]
        } else {
            vec![score[0][0], ways[0][0] as i32]
        }
    }
}