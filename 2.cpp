#include <iostream>
#include <vector>

using namespace std;

long get_mini(const vector<long>& v, long star,long m) {
    long mini = star;
    for (long i = star + 1; i <= m; i += 1)
        if (v[i] < v[mini])
            mini = i;
    return mini;
}

void sort(vector<long>& v,long k,long m) {
    for (long i = k; i<=m; i++)
        swap(v[i], v[get_mini(v, i,m)]);
}

long get_maxi(const vector<long>& v, long star,long m) {
    long maxi = star;
    for (long i = star + 1; i <= m; i += 1)
        if (v[i] > v[maxi])
            maxi = i;
    return maxi;
}

void sort1(vector<long>& v,long k,long m) {
    for (long i = k; i <=m; i++)
        swap(v[i], v[get_maxi(v, i,m)]);
}
void swap(long& a, long& b) {
    long c = a;
    a = b;
    b = c;
}

int main()
{
    long n, k, m, d;
    cin >> n;
    vector<long> v(n);
    for (long i = 0; i < n; i++) {
        cin >> v[i];
    }
    cin >> k >> m >> d;
    k = k - 1;
    m = m - 1;
    if (d == 1)
        sort(v, k, m);
    else
        sort1(v, k, m);
    for (long i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    return 0;
}