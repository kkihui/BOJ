// 이진트리 array로 구현 (class로도 해보기)

#include <iostream>

using namespace std;

struct Node
{
	char data; // 데이터
	char left; // 왼쪽 자식 노드
	char right; // 오른쪽 자식 노드
};

int n;
Node tree[26];

void PreorderTraversal(int idx)
{
	if (tree[idx].data != '.')
	{
		cout << tree[idx].data;
	}

	if (tree[idx].left != '.')
	{

		PreorderTraversal(tree[idx].left - 'A');
	}

	if (tree[idx].right != '.')
	{
		PreorderTraversal(tree[idx].right - 'A');
	}
}

void InorderTraversal(int idx)
{
	if (tree[idx].left != '.')
	{

		InorderTraversal(tree[idx].left - 'A');
	}

	if (tree[idx].data != '.')
	{
		cout << tree[idx].data;
	}

	if (tree[idx].right != '.')
	{
		InorderTraversal(tree[idx].right - 'A');
	}
}

void PostorderTraversal(int idx)
{
	if (tree[idx].left != '.')
	{

		PostorderTraversal(tree[idx].left - 'A');
	}

	if (tree[idx].right != '.')
	{
		PostorderTraversal(tree[idx].right - 'A');
	}

	if (tree[idx].data != '.')
	{
		cout << tree[idx].data;
	}
}

int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		char c;
		cin >> c;
		tree[c - 'A'].data = c;
		cin >> tree[c - 'A'].left >> tree[c - 'A'].right;
	}

	// 전위 순회
	PreorderTraversal(0);
	cout << endl;

	// 중위 순회
	InorderTraversal(0);
	cout << endl;

	// 후위 순회
	PostorderTraversal(0);
	cout << endl;
	
	return 0;
}