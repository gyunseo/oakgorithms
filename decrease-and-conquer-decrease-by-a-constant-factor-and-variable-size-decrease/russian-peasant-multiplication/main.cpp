#include <iostream>
#include <ctime>
using namespace std;

unsigned long long int russian(unsigned long long int a, unsigned long long int b)
{
    unsigned long long int res = 0;
    while (b > 0)
    {
        if (b & 1)
            res = res + a;
        a <<= 1;
        b >>= 1;
    }
    return res;
}

int main()
{
    clock_t start, finish;
    double duration;
    unsigned long long int a, b, res;
    a = 195342362382473513845003428;
    b = 399253634579252174384;
    start = clock();
    res = russian(a, b);
    finish = clock();
    cout << res << endl;
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << "Time: " << duration << " seconds" << endl;
    start = clock();
    res = a * b;
    finish = clock();
    cout << res << endl;
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    cout << "Time: " << duration << " seconds" << endl;
    return 0;
}