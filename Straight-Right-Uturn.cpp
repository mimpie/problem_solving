#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
vector<vector<int>> visited;//셀의 접근방향에 대한 방문여부//미로의 각 요소(배열의 각 요소)는 미로의 크기(size_m) * 행(x) + 열(y)으로 고유하게 식별 가능하므로 다음과 같이 이차원 배열로 나타낼 수 있다. visited[미로의 특정 위치][그 위치에 대한 진입 방향]
vector<vector<int>> map;//미로 정보
int des[2];//출구 좌표
int size_m;//미로 크기
int cnt_case;//테스트 케이스 수
//행(절대좌표기준 방향) 0->우, 1->하, 2->좌, 3->상 | 열(현재방향기준 이동) 0->직진, 1->우회전, 2->U턴 | dx는 행, dy는 열
int dx[][3] = { {0,1,0}, {1,0,-1}, {0,-1,0}, {-1,0,1} };//행과 열을 이용해 현재좌표에서 바라보는 방향에 대해 직진, 우회전, U턴의 이동을 구현
int dy[][3] = { {1,0,-1}, {0,-1,0}, {-1,0,1}, {0,1,0} };//(추가로 도착 후 바라보는 방향은 현재 위치에서 이동한 방향과 같으므로 따로 처리 안해도 됨)
bool isInside(int x, int y) {//이동할 위치가 미로를 벗어나는 지를 확인하는 함수
	return x < size_m&& y < size_m&& x >= 0 && y >= 0;
}
bool CanEscape(int x, int y, int dir) {//세로가 x축 가로가 y축 dir는 현재 보고 있는 방향(절대좌표기준)
	if (x == des[0] && y == des[1])//현재 위치가 출구인지 체크
		return true;
	if (map[x][y] == 1)//현재 위치가 벽인지 체크
		return false;
	if (visited[size_m * x + y][dir] == 2)//현재 셀에 이전과 동일한 방향으로 방문했는지 체크(루프와 U턴 후 다시 U턴을 막음)
		return false;
	map[x][y] = 2;//이동한 경로 표시 위한 표식(로직에 의해 입구와 출구는 0으로 표기됨)
	for (int i = 0; i < 3; i++) {//현재방향 기준 0->직진, 1->우회전, 2->U턴
		int x_new = x + dx[dir][i];//현재좌표, 방향을 기반으로 직진,우회전,U턴에 의해 이동하게 될 행을 계산 
		int y_new = y + dy[dir][i];//현재좌표, 방향을 기반으로 직진,우회전,U턴에 의해 이동하게 될 열을 계산 
		int dir_new = (dir + i) % 4;//현재 방향을 기반으로 직진,우회전,U턴에 의해 바라볼 방향을 계산
		if (!isInside(x_new, y_new))//이동할 위치가 미로를 벗어나는지 체크 벗어난다면 컨티뉴
			continue;
		visited[size_m * x_new + y_new][dir_new]++;//이동할 셀의 접근방향의 카운트 1올림 -> 한번 이용했다는 의미
		if (CanEscape(x_new, y_new, dir_new))//이동할 셀에서 dir_new 방향을 볼때 탈출할 수 있으면 true를 반환  
			return true;
		visited[size_m * x_new + y_new][dir_new]--;//위에서 조건문이 실행되지 않으면 다른 길을 찾아야 하므로 실패했던 경로에 대해 이동했던 정보를 지워줌(정보 무결성 보장)
	}
	return false;//위 과정에서 리턴이 나지 않으면 false리턴
}
int main() {
	ifstream file("input.txt"); //input.txt 파일을 연다. 
	if (file.is_open()) {//파일을 연다
		string line; int val;
		getline(file, line);
		cnt_case = stoi(line);
		for (int i = 0; i < cnt_case; i++) {
			getline(file, line);
			size_m = stoi(line);
			for (int j = 0; j < size_m; j++) {
				getline(file, line);
				istringstream ss(line);
				vector<int> tmp;
				while (ss >> val) {
					tmp.push_back(val);
					visited.push_back({ 0,0,0,0 });
				}
				map.push_back(tmp);
			}
			getline(file, line);
			istringstream ss(line);
			ss >> val; des[0] = val;
			ss >> val; des[1] = val;
			cout << "미로 정보" << endl;
			for (int j = 0; j < size_m; j++) {//입력받은 미로의 정보를 출력
				for (int k = 0; k < size_m; k++)
					cout << map[j][k] << " ";
				cout << endl;
			}
			cout << "출구:" << des[0] << " " << des[1] << endl;//목표위치를 출력
			if (CanEscape(0, 0, 0)) {//시작 셀에서 오른쪽을 보면 동 남으로 모두 이동할 수 있으므로 | 탈출할 수 있다면 탈출 경로를 출력하게 만듬
				cout << "Yes" << endl << "이동 정보" << endl;
				for (int x = 0; x < size_m; x++) {
					for (int y = 0; y < size_m; y++) {
						if (map[x][y] == 2 && visited[size_m * x + y][0] == 0 && visited[size_m * x + y][1] == 0 && visited[size_m * x + y][2] == 0 && visited[size_m * x + y][3] == 0)
							cout << "0 ";
						else
							cout << map[x][y] << " ";
					}
					cout << endl;
				}
				cout << endl << endl;
			}
			else {
				cout << "No" << endl << endl;
			}
			visited.clear();
			map.clear();
		}
		file.close();//파일에서 필요한 내용을 모두 추출했으므로 파일을 닫아준다.
	}
	else {//파일열기에 실패했을때
		cout << "파일경로가 올바른지 확인해주세요.";
		return 1;
	}

	return 0;
}


