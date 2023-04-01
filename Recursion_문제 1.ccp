#include <iostream>
#include <vector>
using namespace std;

vector<int> weight_set;
vector<int> value_set;
vector<int> result_weight;
vector<int> result_value;
int num, std_weight, max_value = 0;
bool* include = new bool[num];

void input() {
	int weight, value;
	cin >> num;
	cin >> std_weight;
	for (int i = 0; i < num; i++) {
		cin >> weight;
		weight_set.push_back(weight);
	}
	for (int i = 0; i < num; i++) {
		cin >> value;
		value_set.push_back(value);
	}
}

void powerSet(int k) {
	if (k == num) {
		int sum_weight = 0;
		int sum_value = 0;
		for (int i = 0; i < num; i++) {
			if (include[i]) {
				sum_weight += weight_set[i];
				sum_value += value_set[i];
			}
		}
		if (sum_weight <= std_weight) {
			if (max_value < sum_value)
				max_value = sum_value;
		}
		return;
	}
	include[k] = false;
	powerSet(k + 1);
	include[k] = true;
	powerSet(k + 1);
}

int main() {
	input();
	powerSet(0);
	cout << max_value;
}
