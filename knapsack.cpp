#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int limit;//무게 제한
vector<int> weight;//물건의 무게를 담는 배열
vector<int> value;//물건의 가치를 담는 배열
int N;//아이템의 갯수
int val_max;//최고 가치, 전역변수라 기본값 0으로 세팅됨
void knapsack(int val, int sum, int level) {//인덱스 level의 물건에 대해 선택여부
	if (sum > limit)//무게가 제한을 초과했을 때
		return;
	if (val_max < val)//현재 가치가 이때까지의 최고 가치보다 클 때 최고 가치를 현재 가치로 갱신
		val_max = val;
	if (level == N)//모든 물건에 대한 선택 여부가 정해졌을 때
		return;
	knapsack(val, sum, level + 1);//현재 물건을 배낭에 넣지 않을 때
	knapsack(val + value[level], sum + weight[level], level + 1);//현재 물건을 배낭에 넣을 때
}
int main() {
	ifstream file("input.txt"); //input.txt 파일을 연다. 
	if (file.is_open()) {//파일을 연다
		string line; int tmp;
		getline(file, line);
		N = stoi(line);
		getline(file, line);
		limit = stoi(line);
		getline(file, line);
		istringstream ss(line);
		while (ss >> tmp) {
			weight.push_back(tmp);
		}
		getline(file, line);
		istringstream ss1(line);
		while (ss1 >> tmp) {
			value.push_back(tmp);
		}
		file.close();//파일에서 필요한 내용을 모두 추출했으므로 파일을 닫아준다.
	}
	else {//파일열기에 실패했을때
		cout << "파일경로가 올바른지 확인해주세요.";
		return 1;
	}

	cout << N << endl;
	cout << limit << endl;
	for (int i : weight)
		cout << i << " ";
	cout << endl;
	for (int j : value) 
		cout << j << " ";
	cout << endl;
	knapsack(0, 0, 0);
	cout << "가격의 최대 합 : " << val_max;


	return 0;
}


