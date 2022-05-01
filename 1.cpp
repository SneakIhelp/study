#include <bits/stdc++.h>

using namespace std;

void menyaem (long&a, long&b)
{
    long c = a; a = b; b = c;
}

long mmm(const vector<long>&v1, long na4, long m)
{
    long mi = na4;
    for (long l = na4+1; l < m; l++)
        if (v1.at(l) < v1.at(mi))
            mi = l;
    return mi;
}
void sorttVverh(vector<long>&v1, long razmer, long k, long m)
{
    for (long l = k; l < m; l++)
            menyaem(v1[l], v1.at(mmm(v1, l, m)));
}

long chislo_raz(vector<long>&v, long num){
    long counter = 1;
    for(int i = 0; i < long(v1.size()); i++){
        if(num == vect[i])
            counter++;
    }
    return counter;
}

bool element_find(vector<long> &v1, long num){
    for(int i = 0; i < long(v1.size()); i++){
        if(v1[i] == num)
            return 1;
    }
    return 0;
}

int main()

{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long razmer = 0, k, chislo = 0;
    bool f = 1;
    cin >> razmer;

    vector<long>v1(razmer), vtemp;

    for (long l = 0; l < razmer; l++)
        cin >> v1.at(l);

    cin >> k;

    for(int j = 0; j < razmer; j++){
        if(chislo_raz(v1, v1[j]) == k and element_find(v1, v1[j]))
            vtemp.push_back(v1[j]);
    }
    
    for(int i = 0; i < long(vtemp.size()); i++){
        cout << vtemp.at(i) << " ";
        f = 0;
    }

    if(f == 1)
        cout << 0;
    return 0;
}
