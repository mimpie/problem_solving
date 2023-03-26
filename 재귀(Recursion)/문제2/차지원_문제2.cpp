#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int DX[4] = {1, 0, -1, 0};
const int DY[4] = {0, -1, 0, 1};

// main에서는 (-1, 0)과 (0, -1)에서 출발했다고 가정하고 ㅎㅎ canExit을 두 번 호출한다.
bool canExit(int n, vector<vector<int>>& map, vector<int>& goal, queue<vector<int>>& q) {
    vector<vector<bool>> visited(n, vector<bool>(n, false));

    while (!q.empty()) {
        auto prev = q.front();
        q.pop();
        if (!visited[prev[0]][prev[1]]) {
            visited[prev[0]][prev[1]] = true;

            for (auto i: {prev[2], (prev[2] + 1) % 4}) {
                auto nx = prev[0] + DX[i];
                auto ny = prev[1] + DY[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n && 
                !visited[nx][ny] && map[nx][ny] == 0) {
                    q.push({nx, ny, i});
                }
            }
        }
    }
    return visited[goal[0]][goal[1]];
}
