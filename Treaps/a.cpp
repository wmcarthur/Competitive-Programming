// Shandom Ruffle
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define F first
#define S second
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

mt19937 rng;

struct treap {
    treap * left, *right;
    int priority;
    int size;
    int value;
    treap(int value) : left(nullptr), right(nullptr), priority(rng()), size(1), value(value) {}
};

void fix(treap* loc) {
    if (!loc) return;
    loc->size = 1 + (loc->left ? loc->left->size : 0) + (loc->right ? loc->right->size : 0);
}

treap* concat(treap* left, treap* right) {
    // if (!left || !right) return left ?: right;
    if (left == nullptr) {
        return right;
    } else if (right == nullptr) {
        return left;
    }

    if (left->priority < right->priority) {
        left->right = concat(left->right, right);
        fix(left);
        return left;
    } else {
        right->left = concat(left, right->left);
        fix(right);
        return right;
    }
}

pair<treap*, treap*> split(treap* root, int after) {
    if(!root) return {nullptr, nullptr};
    int leftSize = root->left ? root->left->size : 0;
    if (after <= leftSize) {
        //Split in left
        auto result = split(root->left, after);
        root->left = result.second;
        fix(root);
        return {result.first, root};
    } else {
        //Split in right
        auto result = split(root->right, after - leftSize - 1);
        root->right = result.first;
        fix(root);
        return {root, result.second};
    }
}

void traverse(treap* root) {
    if (!root) return;
    traverse(root->left);
    cout << root->value << ' ';
    traverse(root->right);
}

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);

    int n;cin >> n;
    treap* root = nullptr;

    for (int i = 1; i <= n; i++) root = concat(root, new treap(i));
    for (int _ = 0; _ < n; _++) {
        int a, b; cin>>a>>b; a--; b--;
        if (b <= a) continue;

        int z = min(n - b, b - a);
        auto [half1, half2] = split(root, b);
        auto [seg1, rest1] = split(half1, a);
        auto [seg2, seg3] = split(rest1, z);
        auto [seg4, seg5] = split(half2, z);
        root = concat(concat(seg1, concat(seg4, seg3)), concat(seg2, seg5));

    }
    traverse(root); cout<<'\n';
}