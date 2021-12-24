// compile with C++11
//

#include<iostream>
#include<thread>
using namespace std;

using namespace std::chrono;                //增加引用空间
template<class T>
void measure(T&& func) {
	auto beg_t = system_clock::now();       //开始时间
	func();								    //执行函数
	auto end_t = system_clock::now();       //结束时间
	duration<double> diff = end_t - beg_t;
	printf("performTest total time: ");
	cout << diff.count()<<endl;
}


void NumberAdd(long start, long end, long &ans) {
	int sum = 0;
	for (long i = start; i < end; i++) 
		sum = sum + 1;
	ans = sum;
}




int main() {
	long times = 500000000;
	measure([times]() {           //双线程
		long ans1 = 0, ans2 = 0;
		thread t1 = thread(NumberAdd, 0, times / 2, ref(ans1));
		thread t2 = thread(NumberAdd, times / 2, times, ref(ans2));
		t1.join();
		t2.join();
		cout << "result of two treads: " << ans1 + ans2 << endl;
		}
	);
	
	measure([times]() {           //单线程
		long ans = 0;
		NumberAdd(0, times, ans);
		cout << "result of single treads: " << ans<< endl;
		}
	);
}
