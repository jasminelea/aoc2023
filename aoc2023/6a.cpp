#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

char buffer[420];

const int DAY = 6;
const int PUZZLE_PART = 2;

void download() {
    sprintf(buffer, "sh download.sh %d", DAY);
    system(buffer);
}

void submit(ll answer) {
    sprintf(buffer, "sh submit.sh %d %d %lld", DAY, PUZZLE_PART, answer);
    system(buffer);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    // download();

    ifstream fin(to_string(DAY) + "input.txt");
    ll out = 0;
    string s, ss;
    // vi v;
    getline(fin, s);
    stringstream sin(s);
    sin >> ss;
    ll n;
    string sss = "", ssss = "";
    while (sin >> ss) {
        sss += ss;
    }
    n = stoll(sss);

    fin >> ss;
    while (fin >> ss) {
        ssss += ss;
    }
    ll v = stoll(ssss);
    ll t = 0;
    for (; t <= v / 2; t++) {
        if (t * (n - t) > v) {
            break;
        }
    }
    out = n + 1 - t * 2;

    cout << out << '\n';

    submit(out);
}